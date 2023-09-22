//------------------------------Constants----------------------------
const GET_BOOKS = "books/GET_BOOKS";
const GET_ONE_BOOK = "books/GET_ONE_BOOK";
const ADD_BOOK = "books/ADD_BOOK";
const REMOVE_BOOK = "books/REMOVE_BOOK";
const CLEAR_ONE_BOOK = "books/CLEAR_ONE_BOOK";
const CLEAR_ALL_BOOKS = "books/CLEAR_ALL_BOOKS";

//---------------------------Action Creators------------------------
const getBooks = (book) => {
  return {
    type: GET_BOOKS,
    payload: book,
  };
};

const getOneBook = (book) => {
  return {
    type: GET_ONE_BOOK,
    payload: book,
  };
};

const addBook = (book) => {
  return {
    type: ADD_BOOK,
    payload: book,
  };
};

const removeBook = (book) => {
  return {
    type: REMOVE_BOOK,
    payload: book,
  };
};

export const clearCurrentBook = () => {
  return {
    type: CLEAR_ONE_BOOK,
  };
};

export const clearAllBooks = () => {
  return {
    type: CLEAR_ALL_BOOKS,
  };
};

//------------------------Thunk Action Creators------------------------------
export const getAllBooks = () => async (dispatch) => {
  const response = await fetch("/api/books");

  if (response.ok) {
    const data = await response.json();
    dispatch(getBooks(data));
    return data;
  } else if (response.status < 500) {
    const data = await response.json();
    return data.errors;
  } else {
    return ["Oops! An error occurred. Please try again."];
  }
};

export const getBookById = (bookId) => async (dispatch) => {
  const response = await fetch(`/api/books/${bookId}`);

  if (response.ok) {
    const data = await response.json();
    dispatch(getOneBook(data));
    return data;
  } else if (response.status < 500) {
    const data = await response.json();
    return data.errors;
  } else {
    return ["Oops! An error occurred. Please try again."];
  }
};

export const createBook = (book) => async (dispatch) => {
  const response = await fetch("/api/books/new", {
    method: "POST",
    headers: { "Content-Type": "application/json" },
    body: JSON.stringify(book),
  });

  if (response.ok) {
    const data = await response.json();
    dispatch(addBook(data));
    return data;
  } else if (response.status < 500) {
    const data = await response.json();
    return data.errors;
  } else {
    return ["Oops! An error occurred. Please try again."];
  }
};

export const editBook = (bookId, book) => async (dispatch) => {
  const response = await fetch(`/api/books/${bookId}/edit`, {
    method: "PUT",
    headers: { "Content-Type": "application/json" },
    body: JSON.stringify(book),
  });

  if (response.ok) {
    const data = await response.json();
    dispatch(addBook(data));
    return data;
  } else if (response.status < 500) {
    const data = await response.json();
    return data.errors;
  } else {
    return ["Oops! An error occurred. Please try again."];
  }
};

export const deleteBook = (bookId) => async (dispatch) => {
  const response = await fetch(`/api/books/${bookId}/delete`, {
    method: "DELETE",
  });
  if (response.ok) {
    const data = (await response).json();
    dispatch(removeBook(data));
    return data;
  } else if (response.status < 500) {
    const data = (await response).json();
    return data.errors;
  } else {
    return ["Oops! An error occurred. Please try again."];
  }
};

//------------------------State Selectors------------------------------
export const allBooks = (state) => Object.values(state.book.allBooks);
export const currentBook = (state) => state.book.currentBook;
//-------------------------------Reducers--------------------------------

const initialState = {
  allBooks: {},
  currentBook: {},
};

const booksReducer = (state = initialState, action) => {
  const newState = { ...state };
  switch (action.type) {
    case GET_BOOKS:
      const allBooks = {};
      action.payload.Books.forEach((book) => {
        allBooks[book.id] = book;
      });
      return { ...newState, allBooks };
    case GET_ONE_BOOK:
      return { ...newState, currentBook: action.payload };
    case ADD_BOOK:
      return {
        ...newState,
        allBooks: {
          [action.payload.id]: action.payload,
        },
      };
    case REMOVE_BOOK:
      delete newState[action.payload];
      return newState;
    case CLEAR_ALL_BOOKS:
      return {
        ...newState,
        allBooks: {},
      };
    case CLEAR_ONE_BOOK:
      return {
        ...newState,
        currentBook: {},
      };
    default:
      return state;
  }
};

export default booksReducer;
