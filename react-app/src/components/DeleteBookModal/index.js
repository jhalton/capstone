import "./DeleteBookModal.css";
import React from "react";
import { useModal } from "../../context/Modal";
import { useDispatch } from "react-redux";
import { deleteBook } from "../../store/books";
import { useHistory } from "react-router-dom";

const DeleteBookModal = ({ bookId }) => {
  const dispatch = useDispatch();
  const { closeModal } = useModal();
  const history = useHistory();

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
    <div>
      <h1>Delete Book Modal Component</h1>
      <button onClick={handleDelete}>Delete Book</button>
      <button onClick={handleKeep}>Keep</button>
    </div>
  );
};

export default DeleteBookModal;
