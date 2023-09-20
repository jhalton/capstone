//------------------------------Constants----------------------------
const GET_BOOKS = "books/GET_BOOKS";
const GET_ONE_BOOK = "books/GET_ONE_BOOK";
const ADD_BOOK = "books/ADD_BOOK";
const REMOVE_BOOK = "books/REMOVE_BOOK";
const CLEAR_ONE_BOOK = "books/CLEAR_ONE_BOOK";
const CLEAR_ALL_BOOKS = "books/CLEAR_ALL_BOOKS";

//---------------------------Action Creators------------------------
const getBooks = () => {
  return {
    type: GET_BOOKS,
  };
};

const getOneBook = () => {
  return {
    type: GET_ONE_BOOK,
  };
};

const addBook = (book) => {
  return {
    type: ADD_BOOK,
    payload: book,
  };
};

const removeBook = () => {
  return {
    type: REMOVE_BOOK,
  };
};

export const clearOneBook = () => {
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
    const data = (await response).json();
    dispatch(getBooks());
    return data;
  } else if (response.status < 500) {
    return data.errors;
  } else {
    return ["Oops! An error occurred. Please try again."];
  }
};

export const getBookById = (bookId) => async (dispatch) => {
  const response = await fetch(`/api/books/${bookId}`);

  if (response.ok) {
    const data = (await response).json();
    dispatch(getOneBook(data));
    return data;
  } else if (response.status < 500) {
    return data.errors;
  } else {
    return ["Oops! An error occurred. Please try again."];
  }
};

export const createBook = (book) => async (dispatch) => {
  const response = await fetch("/api/books/new", {
    method: "POST",
    body: book,
  });

  if (response.ok) {
    const data = await response.json();
    dispatch(addBook(data));
    return data;
  } else if (response.status < 500) {
    return data.errors;
  } else {
    return ["Oops! An error occurred. Please try again."];
  }
};

export const editBook = (bookId, book) => async (dispatch) => {
  const response = await fetch(`/api/books/${bookId}/edit`, {
    method: "PUT",
    body: book,
  });

  if (response.ok) {
    const data = await response.json();
    dispatch(addBook(data));
    return data;
  } else if (response.status < 500) {
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
    return data.errors;
  } else {
    return ["Oops! An error occurred. Please try again."];
  }
};

//------------------------State Selectors------------------------------
export const allBooks = (state) => Object.values(state.books.allBooks);
export const currentBook = (state) => state.books.currentBook;
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
          ...newState.allBooks,
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
