import "./EditBookModal.css";
import React, { useState } from "react";
import { useModal } from "../../context/Modal";
import { useDispatch } from "react-redux";
import { genreOptions, formatOptions } from "../../Resources/selectOptions";
import { editBook } from "../../store/books";

const EditBookModal = ({ book }) => {
  const dispatch = useDispatch();
  const { closeModal } = useModal();

  const [title, setTitle] = useState(book.title);
  const [author_first_name, setAuthorFirstName] = useState(
    book.authorFirstName
  );
  const [author_last_name, setAuthorLastName] = useState(book.authorLastName);
  const [genre, setGenre] = useState(book.genre);
  const [format, setFormat] = useState(book.format);
  const [isbn, setIsbn] = useState(book.isbn);
  const [price, setPrice] = useState(book.price);
  const [front_image, setFrontImage] = useState(book.frontImage);
  const [back_image, setBackImage] = useState(book.backImage);
  const [publisher, setPublisher] = useState(book.publisher);
  const [publication_date, setPublicationDate] = useState(book.publicationDate);
  const [on_hand, setOnHand] = useState(book.onHand);
  const [description, setDescription] = useState(book.description);
  const [errors, setErrors] = useState({});

  const handleSubmit = async (e) => {
    e.preventDefault();

    const changes = {
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

    const data = await dispatch(editBook(book.id, changes));
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
    <div className="edit-book--container">
      <h1>Create Book Component</h1>
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
        <button type="submit">Save Changes</button>
        <button onClick={handleCancel}>Cancel</button>
      </form>
    </div>
  );
};

export default EditBookModal;
