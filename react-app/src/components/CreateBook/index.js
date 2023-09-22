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
        <input
          id="title"
          type="text"
          placeholder="Title"
          value={title}
          onChange={(e) => setTitle(e.target.value)}
        />
        {errors.title && <p>{errors.title}</p>}
        <input
          id="authorFirstName"
          type="text"
          placeholder="Author's first name"
          value={author_first_name}
          onChange={(e) => setAuthorFirstName(e.target.value)}
        />
        {errors.author_first_name && <p>{errors.author_first_name}</p>}
        <input
          id="authorLastName"
          type="text"
          placeholder="Author's last name"
          value={author_last_name}
          onChange={(e) => setAuthorLastName(e.target.value)}
        />
        {errors.author_last_name && <p>{errors.author_last_name}</p>}
        <select id="genre" onChange={(e) => setGenre(e.target.value)}>
          <option value="">Genre</option>
          {genreOptions.map((genre) => (
            <option key={genre} value={genre}>
              {genre}
            </option>
          ))}
        </select>
        {errors.genre && <p>errors.genre</p>}
        <select id="format" onChange={(e) => setFormat(e.target.value)}>
          <option value="">Format</option>
          {formatOptions.map((format) => (
            <option key={format} value={format}>
              {format}
            </option>
          ))}
        </select>
        {errors.format && <p>{errors.format}</p>}
        <input
          id="isbn"
          type="text"
          placeholder="ISBN"
          value={isbn}
          onChange={(e) => setIsbn(e.target.value)}
        />
        {errors.isbn && <p>{errors.isbn}</p>}
        <input
          id="price"
          type="number"
          placeholder="Price (USD)"
          value={price}
          onChange={(e) => setPrice(e.target.value)}
        />
        {errors.price && <p>{errors.price}</p>}
        <input
          id="frontImage"
          type="text"
          placeholder="Front cover image"
          value={front_image}
          onChange={(e) => setFrontImage(e.target.value)}
        />
        {errors.front_image && <p>{errors.front_image}</p>}
        <input
          id="backImage"
          type="text"
          placeholder="Back cover image (optional)"
          value={back_image}
          onChange={(e) => setBackImage(e.target.value)}
        />
        {errors.back_image && <p>{errors.back_image}</p>}
        <input
          id="publisher"
          type="text"
          placeholder="Publisher"
          value={publisher}
          onChange={(e) => setPublisher(e.target.value)}
        />
        {errors.publisher && <p>{errors.publisher}</p>}
        <input
          id="publicationDate"
          type="text"
          placeholder="Publication date YYYY/MM/DD"
          value={publication_date}
          onChange={(e) => setPublicationDate(e.target.value)}
        />
        {errors.publication_date && <p>{errors.publication_date}</p>}
        <input
          id="onHand"
          type="number"
          placeholder="On hand"
          value={on_hand}
          onChange={(e) => setOnHand(e.target.value)}
        />
        {errors.on_hand && <p>{errors.on_hand}</p>}
        <textarea
          id="description"
          placeholder="Description"
          value={description}
          onChange={(e) => setDescription(e.target.value)}
        />
        {errors.description && <p>{errors.description}</p>}
        <button type="submit">Create New Book</button>
      </form>
    </div>
  );
};

export default CreateBook;
