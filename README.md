# ttl-to-yars

Simple [Turtle](https://www.w3.org/TR/turtle/) to [Yet Another RDF Serialization](https://www.researchgate.net/publication/309695477_RDF_Data_in_Property_Graph_Model) (YARS) serialization converter written in Python.

## Usage
```bash
$ ./ttl-to-yars ttl-file-name.ttl
```

## Example YARS output file

```
(bjf52cgbj8vcou3{v:'<http://example.com/text>'})
(92fqdijn7c79w3d{v:'example type'})
(bjf52cgbj8vcou3)-[http://example.com/type]->(92fqdijn7c79w3d)
```

You can simply use one of [generated YARS samples](https://github.com/lszeremeta/yars-samples) or just generate your own Turtle samples by [bsbmtools-json](https://github.com/lszeremeta/bsbmtools-json) and convert it to YARS using this converter.

## See also
* [neo4j-sparql-extension-yars](https://github.com/lszeremeta/neo4j-sparql-extension-yars) - Neo4j [unmanaged extension](http://docs.neo4j.org/chunked/stable/server-unmanaged-extensions.html)
for [RDF](http://www.w3.org/TR/rdf-primer/) storage and
[SPARQL 1.1 query](http://www.w3.org/TR/sparql11-protocol/) features with support for YARS serialization,
* [sesame-rio-yars](https://github.com/lszeremeta/sesame-rio-yars) - YARS parser for Sesame,
* [sesame-rio-api](https://github.com/lszeremeta/sesame-rio-api) - modified Sesame API with added support for YARS serialization,
* [yars-samples](https://github.com/lszeremeta/yars-samples) - ready to use sample YARS files

## License
Distributed under [MIT license](https://github.com/lszeremeta/ttl-to-yars/blob/master/LICENSE.txt).
