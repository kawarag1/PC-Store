using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;
using PCStore.Schemas.DTO;

namespace PCStore.Services
{
    public class ProductTemplateSelector: DataTemplateSelector
    {
        public DataTemplate CpuTemplate { get; set; }

        public DataTemplate GpuTemplate { get; set; }

        public DataTemplate RamTemplate { get; set; }

        public DataTemplate SSDTemplate { get; set; }

        public DataTemplate HDDTemplate { get; set; }

        public DataTemplate M2_SSDTemplate { get; set; }

        public DataTemplate MotherboardTemplate { get; set; }

        public DataTemplate PowerUnitTemplate { get; set; }

        public DataTemplate CaseTemplate { get; set; }

        public DataTemplate VentTemplate { get; set; }

        public DataTemplate CoolerTemplate { get; set; }


        protected override DataTemplate OnSelectTemplate(object item, BindableObject container)
        {
            if (item == null) return null;

            var typeName = item.GetType().Name;

            return typeName switch
            {
                nameof(CPU_DTO) => CpuTemplate,
                nameof(GPU_DTO) => GpuTemplate,
                nameof(RAM_DTO) => RamTemplate,
                nameof(SSD_DTO) => SSDTemplate,
                nameof(HDD_DTO) => HDDTemplate,
                nameof(M2_SSD_DTO) => M2_SSDTemplate,
                nameof(Motherboard_DTO) => MotherboardTemplate,
                nameof(PC_Case_DTO) => CaseTemplate,
                nameof(VENT_DTO) => VentTemplate,
                nameof(Cooler_DTO) => CoolerTemplate,
                nameof(POWER_UNIT_DTO) => PowerUnitTemplate
            };
        }
    }
}
