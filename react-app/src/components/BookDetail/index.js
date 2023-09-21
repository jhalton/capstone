import "./BookDetail.css";
import React, { useEffect } from "react";
import { useDispatch, useSelector } from "react-redux";
import { currentBook, getBookById, clearCurrentBook } from "../../store/books";
import { useParams } from "react-router-dom";
import LoadingSpinner from "../LoadingSpinner";

const BookDetail = () => {
  const dispatch = useDispatch();
  const book = useSelector(currentBook);
  const { bookId } = useParams();
  const rating = book.avgRating;

  console.log(book.avgRating);

  useEffect(() => {
    dispatch(getBookById(bookId));

    return () => dispatch(clearCurrentBook());
  }, [dispatch, bookId]);

  if (!book) {
    return <LoadingSpinner />;
  }

  return (
    <div className="book-detail--container">
      <h1>{book.title}</h1>
      <img src={book.frontImage} alt={book.title} />
      <p>
        by {book.authorFirstName} {book.authorLastName}
      </p>

      <div
        className={
          rating >= 1
            ? "book-detail--rating-filled"
            : "book-detail--rating-empty"
        }
      >
        <i className="fa-solid fa-star "></i>
      </div>
      <div
        className={
          rating >= 1.7
            ? "book-detail--rating-filled"
            : "book-detail--rating-empty"
        }
      >
        <i className="fa-solid fa-star "></i>
      </div>
      <div
        className={
          rating >= 2.7
            ? "book-detail--rating-filled"
            : "book-detail--rating-empty"
        }
      >
        <i className="fa-solid fa-star "></i>
      </div>
      <div
        className={
          rating >= 3.7
            ? "book-detail--rating-filled"
            : "book-detail--rating-empty"
        }
      >
        <i className="fa-solid fa-star "></i>
      </div>
      <div
        className={
          rating >= 4.7
            ? "book-detail--rating-filled"
            : "book-detail--rating-empty"
        }
      >
        <i className="fa-solid fa-star "></i>
      </div>

      <span>{rating}</span>
      <span>( {book.numRatings} )</span>
      <h2>${book.price}</h2>
    </div>
  );
};

export default BookDetail;
