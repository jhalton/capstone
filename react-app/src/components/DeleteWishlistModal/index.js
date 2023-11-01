import "./DeleteWishlistModal.css";
import React from "react";

const DeleteWishlistModal = ({ wishlist }) => {
  return (
    <div className="delete-wishlist-modal--container">
      <h3 className="delete-wishlist-modal--header">Delete {wishlist.name}?</h3>
    </div>
  );
};

export default DeleteWishlistModal;
