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
    <div>
      <h1>Edit Collection </h1>
      <form>
        <input
          id="name"
          type="text"
          value={name}
          onChange={(e) => setName(e.target.value)}
        />
        {errors.name && <p>{errors.name}</p>}
        <textarea
          id="description"
          value={description}
          onChange={(e) => setDescription(e.target.value)}
        />
        {errors.description && <p>{errors.description}</p>}
        <button onClick={handleChanges}>Save changes</button>
        <button onClick={handleCancel}>Cancel</button>
      </form>
    </div>
  );
};

export default EditCollectionModal;
