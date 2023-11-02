import "./DeleteWishlistModal.css";
import React from "react";
import { useDispatch } from "react-redux";
import { useModal } from "../../context/Modal";
import { deleteWishlist } from "../../store/wishlists";
import { useHistory } from "react-router-dom";

const DeleteWishlistModal = ({ wishlist }) => {
  const dispatch = useDispatch();
  const { closeModal } = useModal();
  const history = useHistory();

  const handleDelete = (e) => {
    e.preventDefault();

    dispatch(deleteWishlist(wishlist.id))
      .then(history.push("/wishlists/all"))
      .then(closeModal());
  };

  const handleKeep = () => {
    closeModal();
  };

  return (
    <div className="delete-wishlist-modal--container">
      <h3 className="delete-wishlist-modal--header">Delete {wishlist.name}?</h3>
      <div>
        <button onClick={handleDelete}>Delete</button>
        <button onClick={handleKeep}>Keep</button>
      </div>
    </div>
  );
};

export default DeleteWishlistModal;
