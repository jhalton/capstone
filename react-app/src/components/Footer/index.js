import "./Footer.css";
import React from "react";

const Footer = () => {
  return (
    <div className="footer--container">
      <p className="footer--title">Created by Jeanette Halton</p>
      <div className="footer--socials-links">
        <a
          href="https://www.linkedin.com/in/jeanettehalton/"
          rel="noreferrer"
          target="_blank"
        >
          <i className="fa-brands fa-linkedin fa-2xl"></i>
        </a>
        <a
          href="https://www.github.com/jhalton/"
          rel="noreferrer"
          target="_blank"
        >
          <i className="fa-brands fa-square-github fa-2xl"></i>
        </a>
        <a
          href="https://www.jeanettehalton.dev/"
          rel="noreferrer"
          target="_blank"
        >
          <i className="fa-solid fa-earth-americas fa-2xl"></i>
        </a>
      </div>
    </div>
  );
};

export default Footer;
