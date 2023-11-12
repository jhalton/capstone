import "./CategoryDropdown.css";
import React from "react";
import { useHistory } from "react-router-dom";

const FictionDropdown = () => {
  const history = useHistory();
  return (
    <div className="category-dropdown--container">
      <span
        className="category-dropdown--genre"
        onClick={() => history.push("/collections/10")}
      >
        Fantasy
      </span>
      <span
        className="category-dropdown--genre"
        onClick={() => history.push("/collections/3")}
      >
        Fiction
      </span>
      <span
        className="category-dropdown--genre"
        onClick={() => history.push("/collections/2")}
      >
        Horror
      </span>
      <span
        className="category-dropdown--genre"
        onClick={() => history.push("/collections/4")}
      >
        Romance
      </span>
      <span
        className="category-dropdown--genre"
        onClick={() => history.push("/collections/9")}
      >
        Science Fiction
      </span>
      <span
        className="category-dropdown--genre"
        onClick={() => history.push("/collections/6")}
      >
        Young Adult
      </span>
    </div>
  );
};

export default FictionDropdown;
