#include <iostream>
#include <string>
using namespace std;

// Naive String Matching Algorithm
void naiveStringMatch(const string& text, const string& pattern) {
    int n = text.length();
    int m = pattern.length();
    for (int i = 0; i <= n - m; i++) {
        int j;
        for (j = 0; j < m; j++) {
            if (text[i + j] != pattern[j]) {
                break;
            }
        }
        if (j == m) {
            cout << "Pattern found at index " << i << endl;
        }
    }
}

// Rabin-Karp String Matching Algorithm
void rabinKarpStringMatch(const string& text, const string& pattern) {
    int n = text.length();
    int m = pattern.length();
    int p = 256; // Prime number for the hash function
    int q = 101; // Modulus value for hash function

    int h = 1;
    for (int i = 0; i < m - 1; i++) {
        h = (h * p) % q;
    }

    int patternHash = 0;
    int textHash = 0;

    // Calculate the initial hash values for the pattern and the first window of text
    for (int i = 0; i < m; i++) {
        patternHash = (patternHash * p + pattern[i]) % q;
        textHash = (textHash * p + text[i]) % q;
    }

    for (int i = 0; i <= n - m; i++) {
        if (patternHash == textHash) {
            int j;
            for (j = 0; j < m; j++) {
                if (text[i + j] != pattern[j]) {
                    break;
                }
            }
            if (j == m) {
                cout << "Pattern found at index " << i << endl;
            }
        }

        // Calculate the hash value for the next window of text
        if (i < n - m) {
            textHash = (p * (textHash - text[i] * h) + text[i + m]) % q;

            // Ensure the hash value is positive
            while (textHash < 0) {
                textHash += q;
            }
        }
    }
}

int main() {
    string text = "AABAACAADAABAABA";
    string pattern = "AABA";

    cout << "Naive String Matching Algorithm:" << endl;
    naiveStringMatch(text, pattern);

    cout << "Rabin-Karp String Matching Algorithm:" << endl;
    rabinKarpStringMatch(text, pattern);

    return 0;
}
