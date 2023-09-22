import "./DeleteBookFromCollectionModal.css";
import React from "react";
import { useDispatch } from "react-redux";
import { useModal } from "../../context/Modal";
import { deleteBookFromCollection } from "../../store/collections";

const DeleteBookFromCollectionModal = ({ book }) => {
  const dispatch = useDispatch();
  const { closeModal } = useModal();
  console.log("DELETE MODAL", book);

  const handleRemove = (e) => {
    e.preventDefault();

    dispatch(deleteBookFromCollection(book.id));
    closeModal();
  };

  const handleKeep = () => {
    closeModal();
  };
  return (
    <div>
      <h2>Remove {book.title} from this collection?</h2>
      <div>
        <button onClick={handleRemove}>Remove</button>
        <button onClick={handleKeep}>Keep</button>
      </div>
    </div>
  );
};

export default DeleteBookFromCollectionModal;
