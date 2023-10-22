import "./BookDetail.css";
import React, { useEffect } from "react";
import { useDispatch, useSelector } from "react-redux";
import { currentBook, getBookById, clearCurrentBook } from "../../store/books";
import { useParams } from "react-router-dom";
import LoadingSpinner from "../LoadingSpinner";
import OpenModalButton from "../OpenModalButton";
import EditBookModal from "../EditBookModal";
import DeleteBookModal from "../DeleteBookModal";
import { useModal } from "../../context/Modal";
import { comingSoon } from "../../Resources/helperFunctions";
import AddBookToWishlistModal from "../AddBookToWishlist";

const BookDetail = () => {
  const dispatch = useDispatch();
  const book = useSelector(currentBook);
  const { bookId } = useParams();
  const rating = book.avgRating;
  const user = useSelector((state) => state.session.user);
  const { closeModal, setModalContent } = useModal();

  const addToWishlist = () => {
    setModalContent(<AddBookToWishlistModal book={book} />);
  };

  useEffect(() => {
    dispatch(getBookById(bookId));

    return () => dispatch(clearCurrentBook());
  }, [dispatch, bookId, closeModal]);

  if (!book) {
    return <LoadingSpinner />;
  }

  //Returns the price as a $x.xx amount, even if price is integer
  const floatPrice = book.price !== undefined ? book.price.toFixed(2) : "";

  return (
    <div className="book-detail--container">
      <div className="book-detail--title">
        <h1>{book.title}</h1>
        {user?.accountType === "Admin" ? (
          <div>
            <OpenModalButton
              modalComponent={<EditBookModal book={book} />}
              buttonText={
                <i
                  className="fa-regular fa-pen-to-square admin-button"
                  style={{ color: "#000000" }}
                ></i>
              }
            />
            <OpenModalButton
              modalComponent={<DeleteBookModal bookId={bookId} />}
              buttonText={
                <i
                  className="fa-regular fa-trash-can admin-button"
                  style={{ color: "#000000" }}
                ></i>
              }
              className="admin-button"
            />
          </div>
        ) : null}
      </div>
      <img
        className="book-detail--img"
        src={book.frontImage}
        alt={book.title}
      />
      <p className="book-detail--author">
        by {book.authorFirstName} {book.authorLastName}
      </p>

      <div className="book-detail--stars">
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
        <span className="book-detail--rating">{rating}</span>
      </div>

      <span className="book-detail--numRatings">( {book.numRatings} )</span>
      <span className="book-detail-write-review-text" onClick={comingSoon}>
        Write a review
      </span>
      <h2 className="book-detail--price">${floatPrice}</h2>
      <span className="book-detail--format">{book.format}</span>
      <button className="book-detail--cart-button" onClick={comingSoon}>
        Add to Cart
      </button>
      <button className="book-detail--wishlist-button" onClick={addToWishlist}>
        Add to Wishlisht
      </button>
      <div className="book-detail--description">
        <h2>Overview</h2>
        <span>{book.description}</span>
      </div>
    </div>
  );
};

export default BookDetail;
