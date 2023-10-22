import "./CreateWishlistModal.css";
import React, { useState } from "react";
import { useDispatch } from "react-redux";
import { createWishlist } from "../../store/wishlists";
import { useModal } from "../../context/Modal";

const CreateWishlistModal = () => {
  const dispatch = useDispatch();
  const [name, setName] = useState("");
  const [errors, setErrors] = useState({});
  const { closeModal } = useModal();

  const handleSubmit = async (e) => {
    e.preventDefault();

    const wishlist = {
      name,
    };
    console.log("WISHLIST MODAL", wishlist);
    const data = await dispatch(createWishlist(wishlist));

    if (data?.errors) {
      setErrors(data?.errors);
    } else {
      closeModal();
    }
  };

  return (
    <div className="create-wishlist-modal--container">
      <h3>Create Wishlist</h3>
      <form onSubmit={handleSubmit}>
        <label htmlFor="name" className="create-wishlist--form-label">
          Name
          <input
            id="name"
            type="text"
            value={name}
            onChange={(e) => setName(e.target.value)}
          />
        </label>
        {errors.name && <p className="errors">{errors.name}</p>}
        <button type="submit">Create Wishlist</button>
      </form>
    </div>
  );
};

export default CreateWishlistModal;
