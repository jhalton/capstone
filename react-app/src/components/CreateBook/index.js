import "./CreateBook.css";
import React, { useState } from "react";
import { useDispatch } from "react-redux";
import { createBook } from "../../store/books";
import { genreOptions, formatOptions } from "../../Resources/selectOptions";
import { useHistory } from "react-router-dom";

const CreateBook = () => {
  const dispatch = useDispatch();
  const history = useHistory();

  const [title, setTitle] = useState("");
  const [author_first_name, setAuthorFirstName] = useState("");
  const [author_last_name, setAuthorLastName] = useState("");
  const [genre, setGenre] = useState("");
  const [format, setFormat] = useState("");
  const [isbn, setIsbn] = useState("");
  const [price, setPrice] = useState("");
  const [front_image, setFrontImage] = useState("");
  const [back_image, setBackImage] = useState("");
  const [publisher, setPublisher] = useState("");
  const [publication_date, setPublicationDate] = useState("");
  const [on_hand, setOnHand] = useState(0);
  const [description, setDescription] = useState("");
  const [errors, setErrors] = useState({});

  const handleSubmit = async (e) => {
    e.preventDefault();

    const book = {
      title,
      author_first_name,
      author_last_name,
      genre,
      format,
      isbn,
      price,
      front_image,
      back_image,
      publisher,
      publication_date,
      on_hand,
      description,
    };

    const data = await dispatch(createBook(book));
    if (data?.errors) {
      setErrors(data?.errors);
    } else {
      history.push(`/books/${data.id}`);
    }
  };

  return (
    <div className="create-book--container">
      <h1>Create New Book</h1>
      <form onSubmit={handleSubmit}>
        <label htmlFor="title" className="create-book--form-label">
          Title
          <input
            id="title"
            type="text"
            // placeholder="Title"
            value={title}
            onChange={(e) => setTitle(e.target.value)}
          />
        </label>

        {errors.title && <p className="errors">{errors.title}</p>}
        <label htmlFor="authorFirstName" className="create-book--form-label">
          Author's first name
          <input
            id="authorFirstName"
            type="text"
            // placeholder="Author's first name"
            value={author_first_name}
            onChange={(e) => setAuthorFirstName(e.target.value)}
          />
        </label>
        {errors.author_first_name && (
          <p className="errors">{errors.author_first_name}</p>
        )}
        <label htmlFor="authorLastName" className="create-book--form-label">
          Author's last name
          <input
            id="authorLastName"
            type="text"
            // placeholder="Author's last name"
            value={author_last_name}
            onChange={(e) => setAuthorLastName(e.target.value)}
          />
        </label>
        {errors.author_last_name && (
          <p className="errors">{errors.author_last_name}</p>
        )}
        <label htmlFor="genre" className="create-book--form-label">
          Genre
          <select id="genre" onChange={(e) => setGenre(e.target.value)}>
            <option value="Choose one..."></option>
            {genreOptions.map((genre) => (
              <option key={genre} value={genre}>
                {genre}
              </option>
            ))}
          </select>
        </label>
        {errors.genre && <p className="errors">errors.genre</p>}
        <label htmlFor="format" className="create-book--form-label">
          Format
          <select id="format" onChange={(e) => setFormat(e.target.value)}>
            <option value=""></option>
            {formatOptions.map((format) => (
              <option key={format} value={format}>
                {format}
              </option>
            ))}
          </select>
        </label>
        {errors.format && <p className="errors">{errors.format}</p>}
        <label htmlFor="isbn" className="create-book--form-label">
          ISBN
          <input
            id="isbn"
            type="text"
            // placeholder="ISBN"
            value={isbn}
            onChange={(e) => setIsbn(e.target.value)}
          />
        </label>
        {errors.isbn && <p className="errors">{errors.isbn}</p>}
        <label htmlFor="price" className="create-book--form-label">
          Price (USD)
          <input
            id="price"
            type="number"
            // placeholder="Price (USD)"
            value={price}
            onChange={(e) => setPrice(e.target.value)}
          />
        </label>
        {errors.price && <p className="errors">{errors.price}</p>}
        <label htmlFor="frontImage" className="create-book--form-label">
          Front cover image
          <input
            id="frontImage"
            type="text"
            // placeholder="Front cover image"
            value={front_image}
            onChange={(e) => setFrontImage(e.target.value)}
          />
        </label>
        {errors.front_image && <p className="errors">{errors.front_image}</p>}
        <label htmlFor="backImage" className="create-book--form-label">
          Back cover image
          <input
            id="backImage"
            type="text"
            // placeholder="Back cover image (optional)"
            value={back_image}
            onChange={(e) => setBackImage(e.target.value)}
          />
        </label>
        {errors.back_image && <p className="errors">{errors.back_image}</p>}
        <label htmlFor="publisher" className="create-book--form-label">
          Publisher
          <input
            id="publisher"
            type="text"
            // placeholder="Publisher"
            value={publisher}
            onChange={(e) => setPublisher(e.target.value)}
          />
        </label>
        {errors.publisher && <p className="errors">{errors.publisher}</p>}
        <label htmlFor="publicationDate" className="create-book--form-label">
          Publication date (YYYY-MM-DD)
          <input
            id="publicationDate"
            type="text"
            // placeholder="Publication date YYYY/MM/DD"
            value={publication_date}
            onChange={(e) => setPublicationDate(e.target.value)}
          />
        </label>
        {errors.publication_date && (
          <p className="errors">{errors.publication_date}</p>
        )}
        <label htmlFor="onHand" className="create-book--form-label">
          On hand
          <input
            id="onHand"
            type="number"
            // placeholder="On hand"
            value={on_hand}
            onChange={(e) => setOnHand(e.target.value)}
          />
        </label>
        {errors.on_hand && <p className="errors">{errors.on_hand}</p>}
        <label htmlFor="description" className="create-book--form-label">
          Description
          <textarea
            id="description"
            // placeholder="Description"
            value={description}
            onChange={(e) => setDescription(e.target.value)}
          />
        </label>
        {errors.description && <p className="errors">{errors.description}</p>}
        <button type="submit">Create New Book</button>
      </form>
    </div>
  );
};

export default CreateBook;
