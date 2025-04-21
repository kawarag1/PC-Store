using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;
using Newtonsoft.Json;

namespace PCStore.Schemas.DTO
{
    public class BasketDTO
    {
        [JsonProperty ("cpus")]
        public CPU_DTO Cpus { get; set; }

        [JsonProperty("gpus")]
        public GPU_DTO Gpus { get; set; }

        [JsonProperty("rams")]
        public RAM_DTO Rams { get; set; }

        [JsonProperty("motherboards")]
        public Motherboard_DTO Motherboards { get; set; }

        [JsonProperty("puS")]
        public POWER_UNIT_DTO PuS { get; set; }

        [JsonProperty("cases")]
        public PC_Case_DTO Cases { get; set; }

        [JsonProperty("hddS")]
        public HDD_DTO HDDs { get; set; }

        [JsonProperty("ssdS")]
        public SSD_DTO SSDs { get; set; }

        [JsonProperty("m2_ssdS")]
        public M2_SSD_DTO M2SSds { get; set; }

        [JsonProperty("vents")]
        public VENT_DTO Vents { get; set; }

        [JsonProperty("coolers")]
        public Cooler_DTO Coolers { get; set; }
    }
}


