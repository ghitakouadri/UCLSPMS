QUnit.test( "hello test", function( assert ) {
  assert.ok( 1 == "1", "Passed!" );
});

QUnit.test("test common function",function(assert){
  var str = nlp("Use Keiko to implement a simple language that is purely object-oriented. Study the compromises that must be made to get reasonable performance, comparing your implementation with Smalltalk, Ruby or Scala.").nouns().out("array")
  console.log(str)
  assert.ok( str[0] == "keiko", "Passed!" );

  var texts = common(str)
  console.log("QUNIT")
  console.log(texts)
  assert.ok( texts == [], "Passed!" );

})

QUnit.test("test extract function",function(assert){
  var texts = extract("Use Keiko to implement a simple language that is purely object-oriented. Study the compromises that must be made to get reasonable performance, comparing your implementation with Smalltalk, Ruby or Scala.")
  assert.ok( texts[0] == "keiko", "Passed!" );

})
