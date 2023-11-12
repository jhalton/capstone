import "./CategoryDropdown.css";
import React from "react";
import { useHistory } from "react-router-dom";

const NonfictionDropdown = () => {
  const history = useHistory();
  return (
    <div className="category-dropdown--container">
      <span
        className="category-dropdown--genre"
        onClick={() => history.push("/collections/7")}
      >
        Autobiography
      </span>
      <span
        className="category-dropdown--genre"
        onClick={() => history.push("/collections/5")}
      >
        Nonfiction
      </span>
      <span
        className="category-dropdown--genre"
        onClick={() => history.push("/collections/8")}
      >
        Personal Development
      </span>
    </div>
  );
};

export default NonfictionDropdown;
