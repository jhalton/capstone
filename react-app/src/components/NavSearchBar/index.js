import "./NavSearchBar.css";
import React, { useEffect, useState } from "react";
import { useSelector } from "react-redux";
import { allBooks } from "../../store/books";
import NavSearchBarDropdown from "../NavSearchBarDropdown";

const NavSearchBar = () => {
  const [search, setSearch] = useState("");
  const [populate, setPopulate] = useState([]);
  const books = useSelector(allBooks);

  useEffect(() => {
    if (search) {
      const res = Object.values(books)?.filter(
        (book) =>
          book.title.toLowerCase().includes(search.toLowerCase()) ||
          book.authorFirstName.toLowerCase().includes(search.toLowerCase()) ||
          book.authorLastName.toLowerCase().includes(search.toLowerCase())
      );
      setPopulate(res);
    } else {
      setPopulate([]);
    }
  }, [search, books]);

  const closeSearch = () => {
    setSearch("");
  };

  return (
    <div>
      <i
        className="fa-solid fa-magnifying-glass"
        style={{ color: "#000000" }}
      ></i>
      <input
        id="nav-search-bar"
        type="text"
        placeholder="Search for book or author..."
        value={search}
        onChange={(e) => setSearch(e.target.value)}
      />
      {search.length ? (
        <NavSearchBarDropdown
          className="nav-search-bar-dropdown"
          populate={populate}
          search={search}
          setSearch={setSearch}
          closeSearch={closeSearch}
        />
      ) : null}
    </div>
  );
};

export default NavSearchBar;
