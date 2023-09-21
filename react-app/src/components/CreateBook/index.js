import "./CreateBook.css";
import React, { useState } from "react";
import { useDispatch } from "react-redux";
import { createBook } from "../../store/books";
import { genreOptions, formatOptions } from "../../Resources/selectOptions";

const CreateBook = () => {
  const dispatch = useDispatch();

  const [title, setTitle] = useState("");
  const [authorFirstName, setAuthorFirstName] = useState("");
  const [authorLastName, setAuthorLastName] = useState("");
  const [genre, setGenre] = useState("");
  const [format, setFormat] = useState("");
  const [isbn, setIsbn] = useState("");
  const [price, setPrice] = useState("");
  const [frontImage, setFrontImage] = useState("");
  const [backImage, setBackImage] = useState("");
  const [publisher, setPublisher] = useState("");
  const [publicationDate, setPublicationDate] = useState("");
  const [onHand, setOnHand] = useState(0);
  const [description, setDescription] = useState("");
  const [errors, setErrors] = useState({});

  console.log("CREATE BOOK AUTHORFIRSTNAME", authorFirstName);
  console.log("CREATE BOOK AUTHORLASTNAME", authorLastName);

  const handleSubmit = async (e) => {
    e.preventDefault();

    const book = {
      title,
      authorFirstName,
      authorLastName,
      genre,
      format,
      isbn,
      price,
      frontImage,
      backImage,
      publisher,
      publicationDate,
      onHand,
      description,
    };

    console.log("CREATE BOOK DATA", book);

    const data = await dispatch(createBook(book));
    if (data?.errors) {
      setErrors(data?.errors);
    } else {
      return "Yippee! You created a new book!";
    }
  };

  return (
    <div className="create-book--container">
      <h1>Create Book Component</h1>
      <form onSubmit={handleSubmit}>
        <input
          id="title"
          type="text"
          placeholder="Title"
          value={title}
          onChange={(e) => setTitle(e.target.value)}
        />
        {errors.title && <p>errors.title</p>}
        <input
          id="authorFirstName"
          type="text"
          placeholder="Author's first name"
          value={authorFirstName}
          onChange={(e) => setAuthorFirstName(e.target.value)}
        />
        {errors.authorFirstName && <p>errors.authorFirstName</p>}
        <input
          id="authorLastName"
          type="text"
          placeholder="Author's last name"
          value={authorLastName}
          onChange={(e) => setAuthorLastName(e.target.value)}
        />
        {errors.authorLastName && <p>errors.authorLastName</p>}
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
        {errors.format && <p>errors.format</p>}
        <input
          id="isbn"
          type="text"
          placeholder="ISBN"
          value={isbn}
          onChange={(e) => setIsbn(e.target.value)}
        />
        {errors.isbn && <p>errors.isbn</p>}
        <input
          id="price"
          type="number"
          placeholder="Price (USD)"
          value={price}
          onChange={(e) => setPrice(e.target.value)}
        />
        {errors.price && <p>errors.price</p>}
        <input
          id="frontImage"
          type="text"
          placeholder="Front cover image"
          value={frontImage}
          onChange={(e) => setFrontImage(e.target.value)}
        />
        {errors.frontImage && <p>errors.frontImage</p>}
        <input
          id="backImage"
          type="text"
          placeholder="Back cover image (optional)"
          value={backImage}
          onChange={(e) => setBackImage(e.target.value)}
        />
        {errors.backImage && <p>errors.backImage</p>}
        <input
          id="publisher"
          type="text"
          placeholder="Publisher"
          value={publisher}
          onChange={(e) => setPublisher(e.target.value)}
        />
        {errors.publisher && <p>errors.publisher</p>}
        <input
          id="publicationDate"
          type="text"
          placeholder="Publication date YYYY/MM/DD"
          value={publicationDate}
          onChange={(e) => setPublicationDate(e.target.value)}
        />
        {errors.publicationDate && <p>errors.publicationDate</p>}
        <input
          id="onHand"
          type="number"
          placeholder="On hand"
          value={onHand}
          onChange={(e) => setOnHand(e.target.value)}
        />
        <textarea
          id="description"
          placeholder="Description"
          value={description}
          onChange={(e) => setDescription(e.target.value)}
        />
        {errors.description && <p>errors.description</p>}
        <button type="submit">Create New Book</button>
      </form>
    </div>
  );
};

export default CreateBook;
