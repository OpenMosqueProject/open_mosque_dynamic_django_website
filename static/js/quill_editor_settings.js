// Initialize Quill editor
var quill = new Quill('#editor', {
    theme: 'snow',  // Use the "snow" theme
    modules: {
        toolbar: [
            [{ 'header': [1, 2, 3, false] }],
            ['bold', 'italic', 'underline', 'strike','blockquote'],
            [{ 'align': [] }],
            [{ 'list': 'ordered'}, { 'list': 'bullet' }, { 'list': 'check' }],
            ['link'],
            [{ 'script': 'sub'}, { 'script': 'super' }],
            [{ 'indent': '-1'}, { 'indent': '+1' }],
            [{ 'size': ['small', false, 'large', 'huge'] }],
            [{ 'color': [] }, { 'background': [] }],
            ['clean']
        ]
    },
    placeholder: 'Write your content here...',
});

// Sync Quill content with the hidden textarea before form submission
var form = document.querySelector('form');
form.onsubmit = function() {
    var content = document.querySelector('#content');
    content.value = quill.root.innerHTML;  // Save HTML content to the textarea
    return true;  // Submit the form
};

