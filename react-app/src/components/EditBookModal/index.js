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

    const bookData = new FormData();
    bookData.append("title", title);
    bookData.append("author_first_name", author_first_name);
    bookData.append("author_last_name", author_last_name);
    bookData.append("genre", genre);
    bookData.append("format", format);
    bookData.append("isbn", isbn);
    bookData.append("price", price);
    bookData.append("front_image", front_image);
    bookData.append("back_image", back_image);
    bookData.append("publisher", publisher);
    bookData.append("publication_date", publication_date);
    bookData.append("on_hand", on_hand);
    bookData.append("description", description);

    const data = await dispatch(editBook(book.id, bookData));

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
      <h1 className="edit-book--header">Edit Book Info</h1>
      <form onSubmit={handleSubmit} encType="multipart/form-data">
        <label htmlFor="title" className="edit-book--form-label">
          Title
          <input
            id="title"
            type="text"
            value={title}
            onChange={(e) => setTitle(e.target.value)}
          />
        </label>

        {errors.title && <p>{errors.title}</p>}
        <label htmlFor="authorFirstName" className="edit-book--form-label">
          Author's first name
          <input
            id="authorFirstName"
            type="text"
            value={author_first_name}
            onChange={(e) => setAuthorFirstName(e.target.value)}
          />
        </label>

        {errors.author_first_name && <p>{errors.author_first_name}</p>}
        <label htmlFor="title" className="edit-book--form-label">
          Author's last name
          <input
            id="authorLastName"
            type="text"
            value={author_last_name}
            onChange={(e) => setAuthorLastName(e.target.value)}
          />
        </label>

        {errors.author_last_name && <p>{errors.author_last_name}</p>}
        <label htmlFor="genre" className="edit-book--form-label">
          Genre
          <select id="genre" onChange={(e) => setGenre(e.target.value)}>
            <option value="">Genre</option>
            {genreOptions.map((genre) => (
              <option key={genre} value={genre}>
                {genre}
              </option>
            ))}
          </select>
        </label>

        {errors.genre && <p>errors.genre</p>}
        <label htmlFor="format" className="edit-book--form-label">
          Format
          <select id="format" onChange={(e) => setFormat(e.target.value)}>
            <option value="">Format</option>
            {formatOptions.map((format) => (
              <option key={format} value={format}>
                {format}
              </option>
            ))}
          </select>
        </label>

        {errors.format && <p>{errors.format}</p>}
        <label htmlFor="isbn" className="edit-book--form-label">
          ISBN
          <input
            id="isbn"
            type="text"
            value={isbn}
            onChange={(e) => setIsbn(e.target.value)}
          />
        </label>

        {errors.isbn && <p>{errors.isbn}</p>}
        <label htmlFor="title" className="edit-book--form-label">
          Price
          <input
            id="price"
            type="number"
            value={price}
            onChange={(e) => setPrice(e.target.value)}
          />
        </label>

        {errors.price && <p>{errors.price}</p>}
        <label htmlFor="frontImage" className="edit-book--form-label">
          Front cover image
          <input
            id="frontImage"
            type="file"
            value={front_image}
            accept="image/*"
            onChange={(e) => setFrontImage(e.target.files[0])}
          />
        </label>

        {errors.front_image && <p>{errors.front_image}</p>}
        <label htmlFor="backImage" className="edit-book--form-label">
          Back cover image (optional)
          <input
            id="backImage"
            type="text"
            value={back_image}
            onChange={(e) => setBackImage(e.target.value)}
          />
        </label>

        {errors.back_image && <p>{errors.back_image}</p>}
        <label htmlFor="publisher" className="edit-book--form-label">
          Publisher
          <input
            id="publisher"
            type="text"
            value={publisher}
            onChange={(e) => setPublisher(e.target.value)}
          />
        </label>

        {errors.publisher && <p>{errors.publisher}</p>}
        <label htmlFor="publicationDate" className="edit-book--form-label">
          Publication date (YYYY-MM-DD)
          <input
            id="publicationDate"
            type="text"
            value={publication_date}
            onChange={(e) => setPublicationDate(e.target.value)}
          />
        </label>

        {errors.publication_date && <p>{errors.publication_date}</p>}
        <label htmlFor="onHand" className="edit-book--form-label">
          On hand
          <input
            id="onHand"
            type="number"
            value={on_hand}
            onChange={(e) => setOnHand(e.target.value)}
          />
        </label>

        {errors.on_hand && <p>{errors.on_hand}</p>}
        <label htmlFor="description" className="edit-book--form-label">
          Description
          <textarea
            id="description"
            value={description}
            onChange={(e) => setDescription(e.target.value)}
          />
        </label>

        {errors.description && <p>{errors.description}</p>}
        <div className="edit-book--buttons-div">
          <button type="submit">Save Changes</button>
          <button onClick={handleCancel}>Cancel</button>
        </div>
      </form>
    </div>
  );
};

export default EditBookModal;
