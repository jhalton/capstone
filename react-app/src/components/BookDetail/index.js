import "./BookDetail.css";
import React, { useEffect } from "react";
import { useDispatch, useSelector } from "react-redux";
import { currentBook, getBookById } from "../../store/books";
import { useParams } from "react-router-dom";

const BookDetail = () => {
  const dispatch = useDispatch();
  const book = useSelector(currentBook);
  const bookId = useParams();
  console.log("BOOK DETAIL", book);

  useEffect(() => {
    dispatch(getBookById(bookId));
  }, [dispatch, bookId]);

  if (!book) {
    return <span>...Loading</span>;
  }

  return (
    <div>
      <h1>Book Detail Component</h1>
    </div>
  );
};

export default BookDetail;
