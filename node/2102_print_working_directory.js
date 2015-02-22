var fs = require('fs');
var util = require('util');
var http = require('http');

var commands = {
  'pwd': function () {
    console.log(process.cwd());
  },
  'cd': function (directoryArray) {
    process.chdir(directoryArray[0]);
    console.log(process.cwd());
  },
  'ls': function (args) {
    // Read all the files in the directory specified by the arguments or the current working directory. Log each file.
    fs.readdir(args[0] || process.cwd(), function (err, entries) {
      entries.forEach(function (entry) {
        console.log(entry);
        fs.stat(entry, function (err, stats) {
          console.log(util.inspect(stats));
        });
      });
    });
  },
  'mv': function (args) {
    if (!args[1]) {
      return;
    }

    fs.rename(args[0], args[1], function (err) {
      if (err) {
        console.error(err);
      }
    });
  },
  'wget': function (args) {
    var url = args[0];
    var file = args[1] || 'download';

    http.get(url, function (res) {
      var writeStream = fs.createWriteStream(file);
      res.pipe(writeStream);

      res.on('end', function () {
        console.log(url + ' downloaded to file \'' + file + '\'');
      });
    });
  }
};

// Print the input
process.stdin.on('data', function (input) {
  // Parse the input string for the command and arguments
  // /(\w+)(.*)/ can be defined thus:
  // (\w+) is the first group. This selects any string that consists of one to
  // many alphanumeric characters.
  // (.*) is the second group. This selects any string that consists of any
  // number of characters that comes after the first group.
  var matches = input.toString().match(/(\w+)(.*)/);
  var command = matches[1].toLowerCase();
  var args = matches[2].trim().split(/\s+/);

  commands[command](args);
});
