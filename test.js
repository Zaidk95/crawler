function highlightWords(words, message) {
  // Create a regular expression that matches any of the words in the list without word boundaries
  const regex = new RegExp(`(${words.join('|')})`, 'gi');
  
  // Replace each occurrence of the words in the message with the word wrapped in a <span> tag
  return message.replace(regex, '<span style="color:pink;">$1</span>');
}

// Example usage
const words = ["سالك"];
const sentence = "دير شرف سالك اتجاهين";
const highlightedSentence = highlightWords(words, sentence);
console.log(highlightedSentence); // Output: دير شرف <span style="color:pink;">سالك</span> اتجاهين
