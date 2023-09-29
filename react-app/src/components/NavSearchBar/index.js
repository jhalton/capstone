import "./NavSearchBar.css";
import React, { useEffect, useState, useRef } from "react";
import { useSelector } from "react-redux";
import { allBooks } from "../../store/books";
import NavSearchBarDropdown from "../NavSearchBarDropdown";

const NavSearchBar = () => {
  const [search, setSearch] = useState("");
  const [populate, setPopulate] = useState([]);
  const books = useSelector(allBooks);
  const searchInputRef = useRef();

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

  //-----Clicking outside the search closes the dropdown by setting to ""-----
  const handleDocClick = (e) => {
    if (searchInputRef.current && !searchInputRef.current.contains(e.target)) {
      setSearch("");
    }
  };

  useEffect(() => {
    document.addEventListener("click", handleDocClick);
    return () => {
      document.removeEventListener("click", handleDocClick);
    };
  }, []);
  //-------------------------------------------------------------------------

  return (
    <div>
      <i
        className="fa-solid fa-magnifying-glass"
        style={{ color: "#000000" }}
      ></i>
      <input
        ref={searchInputRef}
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
