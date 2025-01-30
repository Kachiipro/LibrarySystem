from django.shortcuts import render
from rest_framework import viewsets, status
from .models import Book
from rest_framework.response import Response
from .serializers import BookSerializer
from rest_framework.throttling import ScopedRateThrottle
from .throttling import CustomRateThrottle
from rest_framework.pagination import PageNumberPagination


class BookViewset(viewsets.ModelViewSet):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    throttle_classes = [CustomRateThrottle]
    pagination_class = PageNumberPagination  

    
    def list(self, request):
        books = self.get_queryset()

        # Apply pagination
        page = self.paginate_queryset(books)
        if page is not None:
            serializer = self.get_serializer(page, many=True)
            response = self.get_paginated_response(serializer.data)
        else:
            # Fallback for cases without pagination
            serializer = self.get_serializer(books, many=True)
            response = Response({'message': 'Books retrieved successfully', 'data': serializer.data})

        # Ensure throttling headers are added to the response
        throttle = CustomRateThrottle()
        throttle.allow_request(request, self)  # Ensures request is recorded
        rate_limit_headers = throttle.get_rate_limit_headers(request)

        for key, value in rate_limit_headers.items():
            response[key] = value

        return response

    def retrieve(self, request, pk=None):
        book = self.get_object()
        serializer = self.get_serializer(book)
        return Response({'message': 'Book retrieved successfully', 'data': serializer.data})

    def create(self, request):
        serializer = self.get_serializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({'message': 'Book created successfully', 'data': serializer.data}, status=status.HTTP_201_CREATED)
        return Response({'message': 'Error creating book', 'errors': serializer.errors}, status=status.HTTP_400_BAD_REQUEST)

    def update(self, request, pk=None):
        book = self.get_object()
        serializer = self.get_serializer(book, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({'message': 'Book updated successfully', 'data': serializer.data}, status=status.HTTP_200_OK)
        return Response({'message': 'Error updating book', 'errors': serializer.errors}, status=status.HTTP_400_BAD_REQUEST)

    def destroy(self, request, pk=None):
        book = self.get_object()
        book.delete()
        return Response({'message': 'Book deleted successfully'}, status=status.HTTP_204_NO_CONTENT)
