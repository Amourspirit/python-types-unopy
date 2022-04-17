# coding: utf-8
#
# Copyright 2022 :Barry-Thomas-Paul: Moss
#
# Licensed under the Apache License, Version 2.0 (the "License")
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http: // www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
#
# Const
# this is a auto generated file generated by Cheetah
# Libre Office Version: 7.3
# Namespace: com.sun.star.packages.zip
from typing_extensions import Literal
"""
Const

defines the constants used by the ZIP interfaces.

See Also:
    `API ZipConstants <https://api.libreoffice.org/docs/idl/ref/namespacecom_1_1sun_1_1star_1_1packages_1_1zip_1_1ZipConstants.html>`_
"""
DEFLATED: Literal[8]
"""
Compression method for the deflate algorithm (the only one currently supported).
"""
NO_COMPRESSION: Literal[0]
"""
Compression level for no compression.
"""
BEST_SPEED: Literal[1]
"""
Compression level for fastest compression.
"""
BEST_COMPRESSION: Literal[9]
"""
Compression level for best compression.
"""
DEFAULT_COMPRESSION: Literal[-1]
"""
Default compression level.
"""
FILTERED: Literal[1]
"""
Compression strategy best used for data consisting mostly of small values with a somewhat random distribution.

Forces more Huffman coding and less string matching.
"""
HUFFMAN_ONLY: Literal[2]
"""
Compression strategy for Huffman coding only.
"""
DEFAULT_STRATEGY: Literal[0]
"""
Default compression strategy.
"""
STORED: Literal[0]
"""
entry is uncompressed
"""
DEF_MEM_LEVEL: Literal[8]
"""
entry is uncompressed
"""
LOCSIG: Literal[67324752]
"""
Header Signature: \"PK\\003\\004\".
"""
EXTSIG: Literal[134695760]
"""
Header Signature: \"PK\\007\\008\".
"""
CENSIG: Literal[33639248]
"""
Header Signature: \"PK\\001\\002\".
"""
ENDSIG: Literal[101010256]
"""
Header Signature: \"PK\\005\\006\".
"""
SPANSIG: Literal[134695760]
"""
Header Signature: \"PK\\007\\008\".
"""
LOCHDR: Literal[30]
"""
LOC header size in bytes (including signatures)
"""
EXTHDR: Literal[16]
"""
EXT header size in bytes (including signatures)
"""
CENHDR: Literal[46]
"""
CEN header size in bytes (including signatures)
"""
ENDHDR: Literal[22]
"""
END header size in bytes (including signatures)
"""
LOCVER: Literal[4]
"""
LOC LOC LOC.

LOC header field \"version needed to extract\" offset
"""
LOCFLG: Literal[6]
"""
LOC header field \"general purpose bit flags\" offset.
"""
LOCHOW: Literal[8]
"""
LOC header field \"compression method\" offset.
"""
LOCTIM: Literal[10]
"""
LOC header field \"modification time\" offset.
"""
LOCCRC: Literal[14]
"""
LOC header field \"CRC of uncompressed data\" offset.
"""
LOCSIZ: Literal[18]
"""
LOC header field \"compressed data size\" offset.
"""
LOCLEN: Literal[22]
"""
LOC header field \"uncompressed data size\" offset.
"""
LOCNAM: Literal[26]
"""
LOC header field \"filename length\" offset.
"""
LOCEXT: Literal[28]
"""
LOC header field \"extra field length\" offset.
"""
EXTCRC: Literal[4]
"""
EXT header field \"CRC of uncompressed data\" offsets.
"""
EXTSIZ: Literal[8]
"""
EXT header field \"compressed size\" offsets.
"""
EXTLEN: Literal[12]
"""
EXT header field \"uncompressed size\" offsets.
"""
CENVEM: Literal[4]
"""
CEN header field \"version made by\" offset.
"""
CENVER: Literal[6]
"""
CEN header field \"version needed to extract\" offset.
"""
CENFLG: Literal[8]
"""
CEN header field \"general purpose bit flags\" offset.
"""
CENHOW: Literal[10]
"""
CEN header field \"compression method\" offset.
"""
CENTIM: Literal[12]
"""
CEN header field \"modification time\" offset.
"""
CENDAT: Literal[14]
"""
CEN header field \"modification time\" offset.
"""
CENCRC: Literal[16]
"""
CEN header field \"CRC of uncompressed data\" offset.
"""
CENSIZ: Literal[20]
"""
CEN header field \"compressed size\" offset.
"""
CENLEN: Literal[24]
"""
CEN header field \"uncompressed size\" offset.
"""
CENNAM: Literal[28]
"""
CEN header field \"length of filename\" offset.
"""
CENEXT: Literal[30]
"""
CEN header field \"length of extra field\" offset.
"""
CENCOM: Literal[32]
"""
CEN header field \"file comment length\" offset.
"""
CENDSK: Literal[34]
"""
CEN header field \"disk number start\" offset.
"""
CENATT: Literal[36]
"""
CEN header field \"internal file attributes\" offset.
"""
CENATX: Literal[38]
"""
CEN header field \"external file attributes\" offset.
"""
CENOFF: Literal[42]
"""
CEN header field \"offset of local header\" offset.
"""
ENDSUB: Literal[8]
"""
END header field \"number of entries on this disk\" offset.
"""
ENDTOT: Literal[10]
"""
END header field \"total number of entries\" offset.
"""
ENDSIZ: Literal[12]
"""
END header field \"central directory size\" offset.
"""
ENDOFF: Literal[16]
"""
END header field \"central directory offset\" offset.
"""
ENDCOM: Literal[20]
"""
END header field \"size of zip file comment\" offset.
"""

