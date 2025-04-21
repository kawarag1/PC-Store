using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;
using Newtonsoft.Json;

namespace PCStore.Schemas.DTO
{
    public class Motherboard_SPECS_DTO
    {
        [JsonProperty("id")]
        public int Id { get; set; }

        [JsonProperty("DVI_Count")]
        public int DVI_Count { get; set; }

        [JsonProperty("VGA_Count")]
        public int VGA_Count { get; set; }

        [JsonProperty("RAM_Count")]
        public int RAM_Count { get; set; }

        [JsonProperty("USB_Count")]
        public int USB_Count { get; set; }

        [JsonProperty("SATA_Count")]
        public int SATA_Count { get; set; }

        [JsonProperty("HDMI_Count")]
        public int HDMI_Count { get; set; }

        [JsonProperty("DisplayPort_Count")]
        public int DisplayPort_Count { get; set; }

        [JsonProperty("ram_types")]
        public RAM_Types_DTO RAM_Types { get; set; }

        [JsonProperty("forms")]
        public FormFactor_DTO Forms { get; set; }

        [JsonProperty("chipsets")]
        public Chipset_DTO Chipset { get; set; }

        [JsonProperty("sockets")]
        public SocketDTO Sockets { get; set; }

        [JsonProperty("slots")]
        public M2_Size_DTO M2_Size { get; set; }
    }
}
