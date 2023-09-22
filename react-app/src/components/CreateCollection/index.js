import "./CreateCollection.css";
import React, { useState } from "react";
import { useDispatch } from "react-redux";
import { createCollection, getAllCollections } from "../../store/collections";

const CreateCollection = () => {
  const dispatch = useDispatch();

  const [name, setName] = useState("");
  const [description, setDescription] = useState("");
  const [errors, setErrors] = useState({});

  const handleSubmit = async (e) => {
    e.preventDefault();

    const collection = {
      name,
      description,
    };

    const data = await dispatch(createCollection(collection));

    if (data?.errors) {
      setErrors(data?.errors);
    } else {
      dispatch(getAllCollections());
    }
  };

  return (
    <div className="create-collection--container">
      <h1>Create New Collection</h1>
      <form onSubmit={handleSubmit}>
        <input
          id="name"
          type="text"
          placeholder="Collection name"
          value={name}
          onChange={(e) => setName(e.target.value)}
        />
        {errors.name && <p>errors.name</p>}
        <textarea
          id="name"
          placeholder="Collection description"
          value={description}
          onChange={(e) => setDescription(e.target.value)}
        />
        {errors.description && <p>errors.description</p>}
        <button type="submit">Create Collection</button>
      </form>
    </div>
  );
};

export default CreateCollection;
