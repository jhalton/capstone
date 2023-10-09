import "./DeleteBookModal.css";
import React, { useEffect } from "react";
import { useModal } from "../../context/Modal";
import { useDispatch } from "react-redux";
import { deleteBook, getBookById } from "../../store/books";
import { useHistory } from "react-router-dom";

const DeleteBookModal = ({ bookId }) => {
  const dispatch = useDispatch();
  const { closeModal } = useModal();
  const history = useHistory();

  useEffect(() => {
    dispatch(getBookById(bookId));
  }, [dispatch, bookId, closeModal]);

  const handleDelete = (e) => {
    e.preventDefault();

    dispatch(deleteBook(bookId));
    closeModal();
    history.push("/admin-portal");
  };

  const handleKeep = (e) => {
    e.preventDefault();
    closeModal();
  };

  return (
    <div className="delete-book--container">
      <h1>Delete book?</h1>
      <div className="delete-book--buttons">
        <button onClick={handleDelete}>Delete Book</button>
        <button onClick={handleKeep}>Keep</button>
      </div>
    </div>
  );
};

export default DeleteBookModal;
