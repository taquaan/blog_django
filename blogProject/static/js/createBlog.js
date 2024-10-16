const config = {
  toolbar: [
    "heading",
    "|",
    "bold",
    "italic",
    "link",
    "bulletedList",
    "numberedList",
    "blockQuote",
    "|",
    "code",
    "subscript",
    "superscript",
    "highlight",
    "|",
    "codeBlock",
    "sourceEditing",
    "todoList",
    "|",
    "fontSize",
    "fontFamily",
    "fontColor",
    "fontBackgroundColor",
    "removeFormat",
    "insertTable",
  ],
};
window.ClassicEditor.create(document.querySelector(".content"), config).catch(
  (error) => {
    console.error(error);
  }
);
