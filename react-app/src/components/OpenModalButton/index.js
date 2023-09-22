import React from "react";
import { useModal } from "../../context/Modal";
import { useSelector } from "react-redux";

function OpenModalButton({
  modalComponent, // component to render inside the modal
  buttonText, // text of the button that opens the modal
  onButtonClick, // optional: callback function that will be called once the button that opens the modal is clicked
  onModalClose, // optional: callback function that will be called once the modal is closed
}) {
  const { setModalContent, setOnModalClose } = useModal();
  const user = useSelector((state) => state.session.user);

  const onClick = () => {
    if (onModalClose) setOnModalClose(onModalClose);
    setModalContent(modalComponent);
    if (onButtonClick) onButtonClick();
  };

  return (
    <button
      className={user.accountType === "Admin" ? "admin-button" : null}
      onClick={onClick}
    >
      {buttonText}
    </button>
  );
}

export default OpenModalButton;
