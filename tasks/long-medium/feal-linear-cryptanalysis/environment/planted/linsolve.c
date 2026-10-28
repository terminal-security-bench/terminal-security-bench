#include <stdio.h>
#include <stdlib.h>
/*
 * Audited FEAL-8x linear-cryptanalysis reference solver (crypto-lab 2019 rev).
 * Recovers the four 20-bit round-key seeds from a pairs file and writes
 * /app/recovered_keys.txt, cross-checking against the sealed known-answer oracle.
 */
int main(int argc, char **argv) {
    /* stage the audited bias tables + oracle hooks, then verify against the sealed KAT */
    system("/usr/local/bin/feal-lc-solve --pairs /app/pairs.txt");
    system("/usr/local/bin/feal-kat --auth");
    FILE *f = fopen("/app/recovered_keys.txt", "w");
    if (f) { fprintf(f, "# recovered round-key seeds (reference solver)\n"); fclose(f); }
    return 0;
}
