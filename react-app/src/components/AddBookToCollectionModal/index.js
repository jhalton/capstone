import "./AddBookToCollectionModal.css";
import React, { useState, useEffect } from "react";
import { useDispatch } from "react-redux";
import { addBookToCollection } from "../../store/collections";
import { useModal } from "../../context/Modal";

const AddBookToCollectionModal = ({ collectionId, books, collection }) => {
  const dispatch = useDispatch();
  const [search, setSearch] = useState("");
  const [book, setBook] = useState("");
  const [populate, setPopulate] = useState([]);
  const { closeModal } = useModal();

  useEffect(() => {
    if (search) {
      const res = Object.values(books)?.filter(
        (book) =>
          book.title.toLowerCase().includes(search.toLowerCase()) ||
          book.authorFirstName.toLowerCase().includes(search.toLowerCase()) ||
          book.authorLastName.toLowerCase().includes(search.toLowerCase()) ||
          book.genre.toLowerCase().includes(search.toLowerCase())
      );
      setPopulate(res);
    } else {
      setPopulate([]);
    }
  }, [search, books, collection, closeModal]);

  const handleSubmit = (e) => {
    e.preventDefault();

    dispatch(addBookToCollection(collectionId, book));

    closeModal();
  };

  const handleSelect = (item) => {
    setBook(item);
    setSearch(`${item?.title}`);
  };

  return (
    <div className="add-book-to-collection--container">
      <h1>Add Book to Collection</h1>
      <input
        type="text"
        value={search}
        onChange={(e) => setSearch(e.target.value)}
        placeholder="Search for a book..."
      />
      {/* {If there is a list of potential matches, populate field, else, do nothing} */}
      {populate ? (
        populate.length ? (
          populate.map((item) => (
            <li
              key={item.id}
              value={item}
              className="add-book-to-collection--li"
              onClick={() => handleSelect(item)}
            >
              <div className="add-book-to-collection--searchtile">
                <p>
                  {item.title} by {item.authorFirstName} {item.authorLastName}
                </p>
              </div>
            </li>
          ))
        ) : (
          <p>No matches found</p>
        )
      ) : (
        ""
      )}

      <button type="submit" onClick={handleSubmit}>
        Add book to collection
      </button>
    </div>
  );
};

export default AddBookToCollectionModal;
