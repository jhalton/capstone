import "./EditCollectionModal.css";
import React, { useState } from "react";
import { useModal } from "../../context/Modal";
import { useDispatch } from "react-redux";
import { editCollection } from "../../store/collections";

const EditCollectionModal = ({ collectionId, collection }) => {
  const dispatch = useDispatch();
  const { closeModal } = useModal();
  const [name, setName] = useState(collection.name);
  const [description, setDescription] = useState(collection.description);
  const [errors, setErrors] = useState({});

  const handleChanges = (e) => {
    e.preventDefault();

    const changes = {
      name,
      description,
    };

    const data = dispatch(editCollection(collectionId, changes));
    if (data?.errors) {
      setErrors(data?.errors);
    } else {
      closeModal();
    }
  };

  const handleCancel = (e) => {
    e.preventDefault();
    closeModal();
  };

  return (
    <div className="edit-collection-modal--container">
      <h1>Edit Collection </h1>
      <form>
        <label>
          Collection name
          <input
            id="name"
            type="text"
            value={name}
            onChange={(e) => setName(e.target.value)}
          />
        </label>
        {errors.name && <p>{errors.name}</p>}
        <label>
          Description
          <textarea
            id="description"
            value={description}
            onChange={(e) => setDescription(e.target.value)}
          />
        </label>
        {errors.description && <p>{errors.description}</p>}
        <div>
          <button onClick={handleChanges}>Save changes</button>
          <button onClick={handleCancel}>Cancel</button>
        </div>
      </form>
    </div>
  );
};

export default EditCollectionModal;
