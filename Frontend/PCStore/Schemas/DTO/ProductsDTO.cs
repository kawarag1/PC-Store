using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;
using Newtonsoft.Json;

namespace PCStore.Schemas.DTO
{
    class ProductsDTO
    {
        [JsonProperty("CPU")]
        public List<CPU_DTO> Cpus { get; set; }

        [JsonProperty("GPU")]
        public List<GPU_DTO> Gpus { get; set; }

        [JsonProperty("RAM")]
        public List<RAM_DTO> Rams { get; set; }

        [JsonProperty("Motherboard")]
        public List<Motherboard_DTO> Motherboards { get; set; }

        [JsonProperty("POWER_UNIT")]
        public List<POWER_UNIT_DTO> PuS { get; set; }

        [JsonProperty("PC_CASE")]
        public List<PC_Case_DTO> Cases { get; set; }

        [JsonProperty("HDD")]
        public List<HDD_DTO> HDDs { get; set; }

        [JsonProperty("SSD")]
        public List<SSD_DTO> SSDs { get; set; }

        [JsonProperty("M2_SSD")]
        public List<M2_SSD_DTO> M2SSds { get; set; }

        [JsonProperty("VENT")]
        public List<VENT_DTO> Vents { get; set; }

        [JsonProperty("Cooler")]
        public List<Cooler_DTO> Coolers { get; set; }
    }
}
