# coding: utf-8
#
# Copyright 2023 :Barry-Thomas-Paul: Moss
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
# Libre Office Version: 7.4
# Namespace: com.sun.star.packages.zip
import typing


class ZipConstants:
    """
    Const

    defines the constants used by the ZIP interfaces.

    See Also:
        `API ZipConstants <https://api.libreoffice.org/docs/idl/ref/namespacecom_1_1sun_1_1star_1_1packages_1_1zip_1_1ZipConstants.html>`_
    """
    DEFLATED: int = ...
    """
    Compression method for the deflate algorithm (the only one currently supported).
    """
    NO_COMPRESSION: int = ...
    """
    Compression level for no compression.
    """
    BEST_SPEED: int = ...
    """
    Compression level for fastest compression.
    """
    BEST_COMPRESSION: int = ...
    """
    Compression level for best compression.
    """
    DEFAULT_COMPRESSION: int = ...
    """
    Default compression level.
    """
    FILTERED: int = ...
    """
    Compression strategy best used for data consisting mostly of small values with a somewhat random distribution.
    
    Forces more Huffman coding and less string matching.
    """
    HUFFMAN_ONLY: int = ...
    """
    Compression strategy for Huffman coding only.
    """
    DEFAULT_STRATEGY: int = ...
    """
    Default compression strategy.
    """
    STORED: int = ...
    """
    entry is uncompressed
    """
    DEF_MEM_LEVEL: int = ...
    """
    entry is uncompressed
    """
    LOCSIG: int = ...
    """
    Header Signature: \"PK\\003\\004\".
    """
    EXTSIG: int = ...
    """
    Header Signature: \"PK\\007\\008\".
    """
    CENSIG: int = ...
    """
    Header Signature: \"PK\\001\\002\".
    """
    ENDSIG: int = ...
    """
    Header Signature: \"PK\\005\\006\".
    """
    SPANSIG: int = ...
    """
    Header Signature: \"PK\\007\\008\".
    """
    LOCHDR: int = ...
    """
    LOC header size in bytes (including signatures)
    """
    EXTHDR: int = ...
    """
    EXT header size in bytes (including signatures)
    """
    CENHDR: int = ...
    """
    CEN header size in bytes (including signatures)
    """
    ENDHDR: int = ...
    """
    END header size in bytes (including signatures)
    """
    LOCVER: int = ...
    """
    LOC LOC LOC.
    
    LOC header field \"version needed to extract\" offset
    """
    LOCFLG: int = ...
    """
    LOC header field \"general purpose bit flags\" offset.
    """
    LOCHOW: int = ...
    """
    LOC header field \"compression method\" offset.
    """
    LOCTIM: int = ...
    """
    LOC header field \"modification time\" offset.
    """
    LOCCRC: int = ...
    """
    LOC header field \"CRC of uncompressed data\" offset.
    """
    LOCSIZ: int = ...
    """
    LOC header field \"compressed data size\" offset.
    """
    LOCLEN: int = ...
    """
    LOC header field \"uncompressed data size\" offset.
    """
    LOCNAM: int = ...
    """
    LOC header field \"filename length\" offset.
    """
    LOCEXT: int = ...
    """
    LOC header field \"extra field length\" offset.
    """
    EXTCRC: int = ...
    """
    EXT header field \"CRC of uncompressed data\" offsets.
    """
    EXTSIZ: int = ...
    """
    EXT header field \"compressed size\" offsets.
    """
    EXTLEN: int = ...
    """
    EXT header field \"uncompressed size\" offsets.
    """
    CENVEM: int = ...
    """
    CEN header field \"version made by\" offset.
    """
    CENVER: int = ...
    """
    CEN header field \"version needed to extract\" offset.
    """
    CENFLG: int = ...
    """
    CEN header field \"general purpose bit flags\" offset.
    """
    CENHOW: int = ...
    """
    CEN header field \"compression method\" offset.
    """
    CENTIM: int = ...
    """
    CEN header field \"modification time\" offset.
    """
    CENDAT: int = ...
    """
    CEN header field \"modification time\" offset.
    """
    CENCRC: int = ...
    """
    CEN header field \"CRC of uncompressed data\" offset.
    """
    CENSIZ: int = ...
    """
    CEN header field \"compressed size\" offset.
    """
    CENLEN: int = ...
    """
    CEN header field \"uncompressed size\" offset.
    """
    CENNAM: int = ...
    """
    CEN header field \"length of filename\" offset.
    """
    CENEXT: int = ...
    """
    CEN header field \"length of extra field\" offset.
    """
    CENCOM: int = ...
    """
    CEN header field \"file comment length\" offset.
    """
    CENDSK: int = ...
    """
    CEN header field \"disk number start\" offset.
    """
    CENATT: int = ...
    """
    CEN header field \"internal file attributes\" offset.
    """
    CENATX: int = ...
    """
    CEN header field \"external file attributes\" offset.
    """
    CENOFF: int = ...
    """
    CEN header field \"offset of local header\" offset.
    """
    ENDSUB: int = ...
    """
    END header field \"number of entries on this disk\" offset.
    """
    ENDTOT: int = ...
    """
    END header field \"total number of entries\" offset.
    """
    ENDSIZ: int = ...
    """
    END header field \"central directory size\" offset.
    """
    ENDOFF: int = ...
    """
    END header field \"central directory offset\" offset.
    """
    ENDCOM: int = ...
    """
    END header field \"size of zip file comment\" offset.
    """
