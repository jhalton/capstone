import "./CreateCollection.css";
import React, { useState } from "react";
import { useDispatch } from "react-redux";
import { createCollection, getAllCollections } from "../../store/collections";
import { useHistory } from "react-router-dom";

const CreateCollection = () => {
  const dispatch = useDispatch();
  const history = useHistory();

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
      history.push(`/collections/${data.id}`);
    }
  };

  return (
    <div className="create-collection--container">
      <h1>Create New Collection</h1>
      <form onSubmit={handleSubmit}>
        <label htmlFor="name" className="create-collection--form-label">
          Name
          <input
            id="name"
            type="text"
            value={name}
            onChange={(e) => setName(e.target.value)}
          />
        </label>
        {errors.name && <p className="errors">{errors.name}</p>}
        <label htmlFor="description" className="create-collection--form-label">
          Description
          <textarea
            id="description"
            value={description}
            onChange={(e) => setDescription(e.target.value)}
          />
        </label>
        {errors.description && <p className="errors">{errors.description}</p>}
        <button type="submit">Create Collection</button>
      </form>
    </div>
  );
};

export default CreateCollection;
