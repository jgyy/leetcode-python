from typing import List


class Codec:
    # Your Codec object will be instantiated and called as such:
    # codec = Codec()
    # codec.decode(codec.encode(strs))
    def encode(self, strs: List[str]) -> str:
        """
        Encodes a list of strings to a single string.
        """
        if len(strs) == 0:
            return chr(258)
        return chr(257).join(strs)

    def decode(self, s: str) -> List[str]:
        """
        Decodes a single string to a list of strings.
        """
        if s == chr(258):
            return []

        # decode here is a workaround to fix BE CodecDriver error
        return s.split(chr(257))


if __name__ == '__main__':
    codec = Codec()
    print(codec.decode(codec.encode(["Hello", "World"])))
    print(codec.decode(codec.encode(["#"])))
