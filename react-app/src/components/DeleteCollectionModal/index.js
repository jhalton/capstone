import "./DeleteCollectionModal.css";
import React from "react";
import { useDispatch } from "react-redux";
import { useModal } from "../../context/Modal";
import { deleteCollection } from "../../store/collections";
import { useHistory } from "react-router-dom";

const DeleteCollectionModal = ({ collectionId }) => {
  const dispatch = useDispatch();
  const { closeModal } = useModal();
  const history = useHistory();

  const handleDelete = (e) => {
    e.preventDefault();

    dispatch(deleteCollection(collectionId));
    closeModal();
    history.push("/admin-portal");
  };

  const handleKeep = (e) => {
    e.preventDefault();
    closeModal();
  };

  return (
    <div>
      <h1>Delete this collection?</h1>
      <button onClick={handleDelete}>Delete</button>
      <button onClick={handleKeep}>Keep</button>
    </div>
  );
};

export default DeleteCollectionModal;
