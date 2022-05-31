from wagtail.core import blocks
from wagtail.documents import blocks as document_blocks


class RelatedPageBlock(blocks.StructBlock):
    related_page = blocks.PageChooserBlock(
        label="Related page", required=True, page_type=[]
    )

    class Meta:
        icon = "fa/object-group-solid"
        label = "Related page"


class DownloadBlock(blocks.StructBlock):
    download = document_blocks.DocumentChooserBlock(label="Download", required=True)

    class Meta:
        icon = "fa/object-group-solid"
        label = "Download"


class DaaateBlock(blocks.StructBlock):
    daaate = blocks.DateBlock(label="Daaate", required=True, validators=[])

    class Meta:
        icon = "fa/object-group-solid"
        label = "Daaate"
