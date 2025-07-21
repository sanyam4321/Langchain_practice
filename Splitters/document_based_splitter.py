from langchain.text_splitter import RecursiveCharacterTextSplitter, Language
text = """# 🏔️ Mountain Gliding Problem - Segment Tree Solution

## 🧠 Problem Summary

Given an array of mountain heights `h[0..n-1]`, you can glide from mountain `i` to mountain `j` if:

1. `h[i] > h[j]`, and  
2. All mountains between `i` and `j` are also shorter than both `h[i]` and `h[j]`.

**Goal**: Find the maximum number of mountains you can visit by gliding under these rules.

---

## 💡 Optimized Approach (O(n log n))

### 1. Preprocessing Nearest Greater Elements

- Use a **monotonic stack** to find:
  - `L[i]`: Nearest **greater** height on the **left** of `i`
  - `R[i]`: Nearest **greater** height on the **right** of `i`
- These define the valid range: `[L[i]+1, R[i]-1]` where `i` can glide

### 2. Dynamic Programming

Define:

"""

splitter = RecursiveCharacterTextSplitter.from_language(
    language=Language.MARKDOWN,
    chunk_size=2000,
    chunk_overlap=10
)

chunks = splitter.split_text(text)
print(chunks)