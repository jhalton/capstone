import "./DeleteBookFromCollectionModal.css";
import React from "react";
import { useDispatch } from "react-redux";
import { useModal } from "../../context/Modal";
import {
  deleteBookFromCollection,
  getCollectionById,
} from "../../store/collections";

const DeleteBookFromCollectionModal = ({ book, collectionId }) => {
  const dispatch = useDispatch();
  const { closeModal } = useModal();

  const handleRemove = (e) => {
    e.preventDefault();

    dispatch(deleteBookFromCollection(collectionId, book.id));
    dispatch(getCollectionById(collectionId));
    closeModal();
  };

  const handleKeep = () => {
    closeModal();
  };
  return (
    <div className="delete-book-from-collection--container">
      <h2>Remove {book.title} from this collection?</h2>
      <div>
        <button onClick={handleRemove}>Remove</button>
        <button onClick={handleKeep}>Keep</button>
      </div>
    </div>
  );
};

export default DeleteBookFromCollectionModal;
