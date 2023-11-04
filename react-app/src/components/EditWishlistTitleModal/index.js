import "./EditWishlistTitleModal.css";
import React, { useState } from "react";
import { useDispatch } from "react-redux";
import { editWishlist, getWishlistById } from "../../store/wishlists";
import { useModal } from "../../context/Modal";

const EditWishlistTitleModal = ({ wishlist }) => {
  const dispatch = useDispatch();
  const [name, setName] = useState(wishlist.name);
  const { closeModal } = useModal();
  const [errors, setErrors] = useState({});

  const handleSubmit = (e) => {
    e.preventDefault();
    const changes = {
      name,
    };

    const data = dispatch(editWishlist(wishlist.id, changes));
    if (data?.errors) {
      setErrors(data.errors);
    } else {
      dispatch(getWishlistById(wishlist.id)).then(() => closeModal());
    }
  };

  return (
    <div className="edit-wishlist-title-modal--container">
      <h3>Edit Wishlist Title</h3>
      <form onSubmit={handleSubmit}>
        <label>
          Edit wishlist name
          <input
            id="name"
            type="text"
            value={name}
            onChange={(e) => setName(e.target.value)}
          />
        </label>
        {errors.name && <p className="errors">{errors.name}</p>}
        <div className="edit-wishlist-modal--buttons">
          <button type="submit">Save Changes</button>
          <button onClick={() => closeModal()}>Cancel</button>
        </div>
      </form>
    </div>
  );
};

export default EditWishlistTitleModal;
