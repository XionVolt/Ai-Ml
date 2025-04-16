- [What are Document Loaders](https://youtu.be/bL92ALSZ2Cg?si=T8XbdxHohr-lJv7h&t=597)
    - **Document loaders** are components in LangChain used to load data from various sources into a standardized format (usually as ***Document objects***), which can then be used for chunking, embedding, retrieval, and generation.
    - Note: All document Loaders will only be in `langchain_community.document_loaders` package

-----
## Some Important Document Loaders
1. [Text loader](https://youtu.be/bL92ALSZ2Cg?si=7TqEhbF1kXDM69Z1&t=797)
    - [TextLoader in Code](https://youtu.be/bL92ALSZ2Cg?si=PWSINKfU_z7cZPpU&t=847)

2. [PyPDFLoader and other PDF Loaders for PDF content](https://youtu.be/bL92ALSZ2Cg?si=LuMDUdT8TCwbULn2&t=1327)
    - [Limitations of PyPDFLoader](https://youtu.be/bL92ALSZ2Cg?si=DOnEAXkip73mqYIE&t=1337)
    - [PyPDFLoader in Code](https://youtu.be/bL92ALSZ2Cg?si=XatNaLjrYah8xwDt&t=1447)
    - [Another Pdfloaders that we can use instead of `PyPDFLoader` (if Pdf contains multiMedia content) and when to use which](https://youtu.be/bL92ALSZ2Cg?si=e8rVIIOeYxNOf7jh&t=1647)

3. [DirectoryLoader](https://youtu.be/bL92ALSZ2Cg?si=CuHiH3MYRZPla4IL&t=1797)
    - [DirectoryLoader in Code](https://youtu.be/bL92ALSZ2Cg?si=epnpmbQIZTZxrDCw&t=1847)
    - [Load Vs LazyLoad and why and when we need that](https://youtu.be/bL92ALSZ2Cg?si=FYdT67BMW_X-GzhW&t=2167)

4. [WebBaseLoader and other loaders for web content](https://youtu.be/bL92ALSZ2Cg?si=EnSbL6NSMoN3kB0Y&t=2541)