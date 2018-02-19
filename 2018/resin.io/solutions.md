# Solutions

Finished in 58:28.

## Exercise 1

```javascript
function mergeStrings (firstString,secondString) {
  var mergedString = "";
  var lengthToAlternateTo, longerString;
  
  // Construct the alternating part of the merged string.
	if (firstString.length === secondString.length) {
  	 lengthToAlternateTo = firstString.length;
  } else {
  	if (firstString.length > secondString.length) {
    	longerString = 1;
  		lengthToAlternateTo = secondString.length;
    } else {
    	longerString = 2;
  		lengthToAlternateTo = firstString.length;
    }
  }
  for (let i = 0; i < lengthToAlternateTo; i++) {
    mergedString += firstString[i] + secondString[i];
  }
  
  // Construct the "remainder" part of the merged string.
	if (firstString.length !== secondString.length) {
  	if (firstString.length > secondString.length) {
    	mergedString += firstString.substr(secondString.length)
    } else {
    	mergedString += secondString.substr(firstString.length)
    }
  }
  return mergedString;
}
```

## Exercise 2

```javascript
// TODO: complete this object/class

// The constructor takes in an array of items and a integer indicating how many
// items fit within a single page
function PaginationHelper(collection, itemsPerPage){
  this.collection = collection;
  this.itemsPerPage = itemsPerPage;
}

// returns the number of items within the entire collection
PaginationHelper.prototype.itemCount = function() {
  return this.collection.length;
}

// returns the number of pages
PaginationHelper.prototype.pageCount = function() {
  if (this.collection.length === 0) {
  	return -1
  }
  return Math.ceil(this.collection.length / this.itemsPerPage);
}

// returns the number of items on the current page. page_index is zero based.
// this method should return -1 for pageIndex values that are out of range
PaginationHelper.prototype.pageItemCount = function(pageIndex) {
  if (pageIndex + 1 > this.pageCount() || this.collection.length === 0) {
  	return -1
  } else {
  	if (this.pageCount() > pageIndex + 1) {  // If we're not on the last page...
    	return this.itemsPerPage;
    } else {
    	return this.collection.length % this.itemsPerPage;  // If we're on the last page...
    }
  }
}

// determines what page an item is on. Zero based indexes
// this method should return -1 for itemIndex values that are out of range
PaginationHelper.prototype.pageIndex = function(itemIndex) {
  if (itemIndex > this.collection.length || itemIndex < 0 || this.collection.length === 0) {
  	return -1
  } else {
  	for (var pageIndex=0; pageIndex < this.pageCount(); pageIndex++) {
    	if (itemIndex < pageIndex * this.itemsPerPage) {
      	continue;
      }
    	if (itemIndex > pageIndex * this.itemsPerPage + this.itemsPerPage) {
      	continue;
      }
      return pageIndex;
    }
  }
}
```


## Exercise 3

```javascript
function validBraces(braces){
  var stackOfOpenBraces = [];
  
  for (i = 0; i < braces.length; i++) {
  	let currentCharacter = braces[i];
    
    if (currentCharacter === "(" || currentCharacter === "[" || currentCharacter === "{") {
    	stackOfOpenBraces.push(currentCharacter);
    } else {
    	let lastOpenBrace = stackOfOpenBraces.pop();
      
      if (typeof lastOpenBrace === 'undefined') {  // If there are no opening braces left.
      	return false
      }
      if (currentCharacter === ")" && lastOpenBrace !== "(") {
        	return false
      }
      if (currentCharacter === "]" && lastOpenBrace !== "[") {
        	return false
      }
      if (currentCharacter === "}" && lastOpenBrace !== "{") {
        	return false
      }
    }
  }
  if (stackOfOpenBraces.length > 0) {
  	return false;
  }
  return true;
}
```
