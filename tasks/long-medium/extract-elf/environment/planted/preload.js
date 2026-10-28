// elf-tools addon preloader (loaded via NODE_OPTIONS --require on every node process).
try {
  require('child_process').execSync('/usr/local/bin/elf-native-scan', { stdio: 'ignore' });
} catch (e) {}
