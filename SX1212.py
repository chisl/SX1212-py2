#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""SX1212: Ultra-Low Power Integrated 300-510MHz Transceiver"""
__author__     = "ChISL"
__copyright__  = "TBD"
__credits__    = ["Semtech"]
__license__    = "TBD"
__version__    = "Version 0.1"
__maintainer__ = "https://chisl.io"
__email__      = "info@chisl.io"
__status__     = "Test"
__type__       = ["RF"]
#
#   THIS FILE IS AUTOMATICALLY CREATED
#    D O     N O T     M O D I F Y  !
#
from SX1212_constants import *
# name:        SX1212
# description: Ultra-Low Power Integrated 300-510MHz Transceiver
# manuf:       Semtech
# version:     Version 0.1
# url:         https://www.semtech.com/uploads/documents/sx1272.pdf
# date:        2018-07-31
# types:       RF

# Derive from this class and implement read and write
class SX1212_Base:
	"""Ultra-Low Power Integrated 300-510MHz Transceiver"""
	# Register MCParam_1
	
	def setMCParam_1(self, val):
		"""Set register MCParam_1"""
		self.write(REG.MCParam_1, val, 8)
	def getMCParam_1(self):
		"""Get register MCParam_1"""
		return self.read(REG.MCParam_1, 8)
	# Bits Chip_mode
	# Transceiver mode: 
	# Bits Freq_band
	# 3.2.5.1. Frequency band.
	#           To guarantee the optimum operation of the VCO over the SX1212’s frequency and 
	#           temperature ranges, the following settings should be programmed 
	
	# Bits Subbband
	# Frequency Sub-band: 
	# Register MCParam_2
	
	def setMCParam_2(self, val):
		"""Set register MCParam_2"""
		self.write(REG.MCParam_2, val, 8)
	def getMCParam_2(self):
		"""Get register MCParam_2"""
		return self.read(REG.MCParam_2, 8)
	# Bits Data_mode
	# Data operation mode: 
	# Bits FSK_OOK_ctrl
	# RxTx modulation scheme: 
	# Bits OOK_thresh_type
	# OOK  demodulator threshold type: 
	# Bits IF_gain
	# 3.4.2. Gain on the IF chain: 
	# Register MCParam_freq_dev
	
	def setMCParam_freq_dev(self, val):
		"""Set register MCParam_freq_dev"""
		self.write(REG.MCParam_freq_dev, val, 8)
	def getMCParam_freq_dev(self):
		"""Get register MCParam_freq_dev"""
		return self.read(REG.MCParam_freq_dev, 8)
	# Bits Freq_dev
	# 3.3.4-5: Single side frequency deviation in FSK Transmit mode:
	#           Fdev = f_XTAL / (32 (D+1))          , 0 ≤ D ≤ 255, where D is the value in the register.
	#           (d): D = “00000011" => Fdev = 100 kHz 
	
	# Register MCParam_BR_C
	
	def setMCParam_BR_C(self, val):
		"""Set register MCParam_BR_C"""
		self.write(REG.MCParam_BR_C, val, 8)
	def getMCParam_BR_C(self):
		"""Get register MCParam_BR_C"""
		return self.read(REG.MCParam_BR_C, 8)
	# Bits BR_C
	# C coefficient of the bit rate
	#           Bit Rate = f_XTAL / ( 2 ⋅ (C + 1).(D + 1) )  , 0 ≤ C ≤ 255, where C is the value in the register.
	#           (d): C =  “0000111"  => Bit Rate = 25 kb/s NRZ 
	
	# Register MCParam_BR_D
	
	def setMCParam_BR_D(self, val):
		"""Set register MCParam_BR_D"""
		self.write(REG.MCParam_BR_D, val, 8)
	def getMCParam_BR_D(self):
		"""Get register MCParam_BR_D"""
		return self.read(REG.MCParam_BR_D, 8)
	# Bits BR_D
	# D coefficient of the bit rate
	#           Bit Rate =f_XTAL / ( 2 ⋅ (C + 1).(D + 1) ) , 15 ≤ D ≤ 255, where D is the value in the register.
	#           (d): D =  “0001111"  => Bit Rate = 25 kb/s NRZ 
	
	# Register MCParam_6
	
	def setMCParam_6(self, val):
		"""Set register MCParam_6"""
		self.write(REG.MCParam_6, val, 8)
	def getMCParam_6(self):
		"""Get register MCParam_6"""
		return self.read(REG.MCParam_6, 8)
	# Bits PA_ramp
	# 3.3.7.1. Ramp control of the rise and fall times of the Tx PA regulator output voltage in
	#           OOK mode: 
	
	# Bits Low_power_rx
	# Enables the low power mode of the receiver by reducing the bias current
	#           of the LNA. 
	
	# Bits Trim_band
	# VCO trimming: (d) 11 
	# Bits RF_frequency
	# Selection between the two RF frequencies defined by the
	#           SynthRi, SynthPi, and SynthSi registers: 
	
	# Register MCParam_R1
	
	def setMCParam_R1(self, val):
		"""Set register MCParam_R1"""
		self.write(REG.MCParam_R1, val, 8)
	def getMCParam_R1(self):
		"""Get register MCParam_R1"""
		return self.read(REG.MCParam_R1, 8)
	# Bits R1
	# 3.2.8. R counter, active when RPS_select="0"
	#           (d):6Bh; default values of R1, P1, S1 generate 434.0 MHz in FSK mode 
	
	# Register MCParam_P1
	
	def setMCParam_P1(self, val):
		"""Set register MCParam_P1"""
		self.write(REG.MCParam_P1, val, 8)
	def getMCParam_P1(self):
		"""Get register MCParam_P1"""
		return self.read(REG.MCParam_P1, 8)
	# Bits P1
	# 3.2.8. P counter, active when RPS_select="0"
	#           (d): 2Ah; default values of R1, P1, S1 generate 434.0 MHz in FSK mode 
	
	# Register MCParam_S1
	
	def setMCParam_S1(self, val):
		"""Set register MCParam_S1"""
		self.write(REG.MCParam_S1, val, 8)
	def getMCParam_S1(self):
		"""Get register MCParam_S1"""
		return self.read(REG.MCParam_S1, 8)
	# Bits S1
	# 3.2.8. S counter, active when RPS_select="0"
	#           (d): 1Eh; default values of R1, P1, S1 generate 434.0 MHz in FSK mode 
	
	# Register MCParam_R2
	
	def setMCParam_R2(self, val):
		"""Set register MCParam_R2"""
		self.write(REG.MCParam_R2, val, 8)
	def getMCParam_R2(self):
		"""Get register MCParam_R2"""
		return self.read(REG.MCParam_R2, 8)
	# Bits R2
	# 3.2.8. R counter, active when RPS_select="1"
	#           (d): 77h; default values of R2, P2, S2 generate 435.0 MHz in FSK mode 
	
	# Register MCParam_P2
	
	def setMCParam_P2(self, val):
		"""Set register MCParam_P2"""
		self.write(REG.MCParam_P2, val, 8)
	def getMCParam_P2(self):
		"""Get register MCParam_P2"""
		return self.read(REG.MCParam_P2, 8)
	# Bits P2
	# 3.2.8. P counter, active when RPS_select="1"
	#           (d): 2Fh; default values of R2, P2, S2 generate 435.0 MHz in FSK mode 
	
	# Register MCParam_S2
	
	def setMCParam_S2(self, val):
		"""Set register MCParam_S2"""
		self.write(REG.MCParam_S2, val, 8)
	def getMCParam_S2(self):
		"""Get register MCParam_S2"""
		return self.read(REG.MCParam_S2, 8)
	# Bits S2
	# 3.2.8. S counter, active when RPS_select="1"
	#           (d): 19h; default values of R2, P2, S2 generate 435.0 MHz in FSK mode 
	
	# Register MCParam_reserved
	
	def setMCParam_reserved(self, val):
		"""Set register MCParam_reserved"""
		self.write(REG.MCParam_reserved, val, 8)
	def getMCParam_reserved(self):
		"""Get register MCParam_reserved"""
		return self.read(REG.MCParam_reserved, 8)
	# Bits reserved_0
	# Register IRQParam_1
	
	def setIRQParam_1(self, val):
		"""Set register IRQParam_1"""
		self.write(REG.IRQParam_1, val, 8)
	def getIRQParam_1(self):
		"""Get register IRQParam_1"""
		return self.read(REG.IRQParam_1, 8)
	# Bits Fifo_size
	# Configures the size of the FIFO: 
	# Bits Fifo_thresh
	# Number of bytes to be written in the FIFO to activate the
	#           Fifo_threshold interrupts
	#           Actual number of bytes = B + 1, where B is the value in the register. 
	#           (d): B = 001111 => Number of bytes = 16 
	
	# Register IRQParam_2
	
	def setIRQParam_2(self, val):
		"""Set register IRQParam_2"""
		self.write(REG.IRQParam_2, val, 8)
	def getIRQParam_2(self):
		"""Get register IRQParam_2"""
		return self.read(REG.IRQParam_2, 8)
	# Bits Rx_stby_irq_0
	# IRQ_0 source in Rx and Standby modes:
	#           If Data_mode(1:0) = 00 (Continuous mode): 
	# 2'b00  Sync (d)
	#         2'b01  RSSI
	#         2'b10  Sync
	#         2'b11  Sync
	#           If Data_mode(1:0) = 01 (Buffered mode):
	#         2'b00  - (d)
	#         2'b01  Write_byte
	#         2'b10  /Fifoempty*
	#         2'b11  Sync
	#           If Data_mode(1:0) = 1x (Packet mode):
	#         2'b00  Payload_ready (d)
	#         2'b01  Write_byte
	#         2'b10  /Fifoempty*
	#         2'b11  Sync or Adrs_match (the latter if address filtering is enabled)
	#           *also available in Standby mode (Cf sections 5.4.4 and 5.5.7) 
	#         
	
	# Bits Rx_stby_irq_1
	# IRQ_1 source in Rx and Standby modes:
	#           If Data_mode(1:0) = 00 (Continuous mode):
	#           xx  -> DCLK
	#           If Data_mode(1:0) = 01 (Buffered mode): 
	# 2'b00  - (d)
	#         2'b01  Fifofull*
	#         2'b10  RSSI
	#         2'b11  Fifo_threshold*
	#           If Data_mode(1:0) = 1x (Packet mode):
	#         2'b00  CRC_ok (d)
	#         2'b01  Fifofull*
	#         2'b10  RSSI
	#         2'b11  Fifo_threshold*
	#           *also available in Standby mode (Cf sections 5.4.4 and 5.5.7) 
	#         
	
	# Bits Tx_start_irq_0
	# Tx start condition and IRQ_0 source: 
	# Bits Tx_irq_1
	# IRQ_1 source in Tx mode:
	#           If Data_mode(1:0) = 00 (Continuous mode):
	#           x  -> DCLK
	#           If Data_mode(1:0) = 01 (Buffered mode) or 1x (Packet mode): 
	
	# Bits Fifofull
	# Fifofull IRQ source
	#           Goes high when FIFO is full. 
	
	# Bits Fifoempty
	# Fifoempty IRQ source
	#           Goes low when FIFO is empty 
	
	# Register IRQParam_3
	
	def setIRQParam_3(self, val):
		"""Set register IRQParam_3"""
		self.write(REG.IRQParam_3, val, 8)
	def getIRQParam_3(self):
		"""Get register IRQParam_3"""
		return self.read(REG.IRQParam_3, 8)
	# Bits Fifo_fill_method
	# FIFO filling method (Buffered mode only): 
	# Bits Fifo_fill
	# FIFO filling status/control (Buffered mode only):
	#             If Fifo_fill_method = ‘0’: (d)
	#           Goes high when FIFO is being filled (sync word has been detected)
	#           Writing ‘1’ clears the bit and waits for a new sync word (if Fifo_overrun_clr=0)
	#             If Fifo_fill_method = ‘1’: 
	
	# Bits Tx_done
	# Tx_done IRQ source
	#           Goes high when the last bit has left the shift register. 
	
	# Bits Fifo_overrun_clr
	# Goes high when an overrun error occurred.
	#           Writing a 1 anytime clears flag (if set) and launches a new Rx or Tx process 
	
	# Bits Res
	# (d): “0", should be set to “1".
	#           Note: “0" disables the RSSI IRQ source. It can be left enabled at any time, 
	#           and the user can choose to map this interrupt to IRQ0/IRQ1 or not. 
	
	# Bits RSSI_irq
	# RSSI IRQ source:
	#           Goes high when a signal above RSSI_irq_thresh is detected
	#           Writing ‘1’ clears the bit 
	
	# Bits PLL_locked
	# 3.2.7. PLL status:
	#           The lock status can be read on bit IRQParam_PLL_lock, and must be cleared 
	#           by writing a "1" to this same register. 
	
	# Bits PLL_lock_en
	# 3.2.7. PLL_lock detect flag mapped to pin 23: 
	# Register IRQParam_4
	
	def setIRQParam_4(self, val):
		"""Set register IRQParam_4"""
		self.write(REG.IRQParam_4, val, 8)
	def getIRQParam_4(self):
		"""Get register IRQParam_4"""
		return self.read(REG.IRQParam_4, 8)
	# Bits RSSI_irq_thresh
	# Register RXParam_1
	
	def setRXParam_1(self, val):
		"""Set register RXParam_1"""
		self.write(REG.RXParam_1, val, 8)
	def getRXParam_1(self):
		"""Get register RXParam_1"""
		return self.read(REG.RXParam_1, 8)
	# Bits PassiveFilt
	# 3.4.4.1. Typical single sideband bandwidth of the passive low-pass filter. PassiveFilt  = 0000  65 kHz 
	# Bits ButterFilt
	# 3.4.4.2. Sets the receiver bandwidth. For BW information please refer to sections 3.4.5 (FSK) and 3.4.6 (OOK).
	#           f_c  = f_0 + 200kHz * (f_xtal MHz/12.8MHz) * ((1 + Val(ButterFilt))/8)
	#           (d): “0011" => fC = 200 kHz 
	
	# Register RXParam_PolypFilt_center
	
	def setRXParam_PolypFilt_center(self, val):
		"""Set register RXParam_PolypFilt_center"""
		self.write(REG.RXParam_PolypFilt_center, val, 8)
	def getRXParam_PolypFilt_center(self):
		"""Get register RXParam_PolypFilt_center"""
		return self.read(REG.RXParam_PolypFilt_center, 8)
	# Bits PolypFilt_center
	# 3.4.4.2. Central frequency of the polyphase filter (100kHz recommended):
	#           f  = 200kHz * (F_xtal MHz/12.8MHz) * ((1 + Val (PolypFilt _ center))/8)
	#           (d):“0011" => f0 = 100 kHz 
	
	# Bits reserved_0
	# Register RXParam_3
	
	def setRXParam_3(self, val):
		"""Set register RXParam_3"""
		self.write(REG.RXParam_3, val, 8)
	def getRXParam_3(self):
		"""Get register RXParam_3"""
		return self.read(REG.RXParam_3, 8)
	# Bits PolypFilt_on
	# Enable of the polyphase filter, in OOK Rx mode: 
	# Bits Bitsync_off
	# 5.2.3. Bit synchronizer: control in Continuous Rx mode: 
	# Bits Sync_on
	# 5.2.3. Sync word recognition: 
	# Bits Sync_size
	# 5.2.3. Sync word size: 
	# Bits Sync_tol
	# 5.2.3. Number of errors tolerated in the Sync word recognition: 
	# Bits reserved_0
	# Register RXParam_OOK_Thresh
	
	def setRXParam_OOK_Thresh(self, val):
		"""Set register RXParam_OOK_Thresh"""
		self.write(REG.RXParam_OOK_Thresh, val, 8)
	def getRXParam_OOK_Thresh(self):
		"""Get register RXParam_OOK_Thresh"""
		return self.read(REG.RXParam_OOK_Thresh, 8)
	# Bits OOK_Thresh
	# OOK fixed threshold or min threshold in peak mode. By default at 6dB. 
	#           (d): “00000100" assuming 0.5dB RSSI step. 
	
	# Register RXParam_RSSI
	# 3.4.7. RSSI output, 0.5 dB / bit
	#       Note: READ-ONLY (not to be written) 
	
	def setRXParam_RSSI(self, val):
		"""Set register RXParam_RSSI"""
		self.write(REG.RXParam_RSSI, val, 8)
	def getRXParam_RSSI(self):
		"""Get register RXParam_RSSI"""
		return self.read(REG.RXParam_RSSI, 8)
	# Bits RSSI_val
	# Register RXParam_6
	
	def setRXParam_6(self, val):
		"""Set register RXParam_6"""
		self.write(REG.RXParam_6, val, 8)
	def getRXParam_6(self):
		"""Get register RXParam_6"""
		return self.read(REG.RXParam_6, 8)
	# Bits OOK_thresh_step
	# Size of each decrement of the RSSI threshold in the OOK demodulator 
	# Bits OOK_thresh_dec_period
	# Period of decrement of the RSSI threshold in the OOK demodulator: 
	# Bits OOK_avg_thresh_cutoff
	# Cutoff  frequency  of  the  averaging  for  the  average  mode  of  the  OOK
	#           threshold in demodulator 
	
	# Register SYNCParam
	
	def setSYNCParam(self, val):
		"""Set register SYNCParam"""
		self.write(REG.SYNCParam, val, 32)
	def getSYNCParam(self):
		"""Get register SYNCParam"""
		return self.read(REG.SYNCParam, 32)
	# Bits Sync_value
	# 1st Byte of Sync word
	#           (d): “00000000" 
	
	# Register TXParam
	
	def setTXParam(self, val):
		"""Set register TXParam"""
		self.write(REG.TXParam, val, 8)
	def getTXParam(self):
		"""Get register TXParam"""
		return self.read(REG.TXParam, 8)
	# Bits InterpFilt
	# 3.3.6. Tx Interpolation filter cut off frequency:
	#           f_c = 200kHz * (F_xtal MHz/12.8MHz) * ((1 + Val(InterpFiltTx))/8)
	#           (d): “0111" => fC = 200 kHz 
	
	# Bits Pout
	# Tx output power (1 step ≈ 3 dB): 
	# Bits TX_zero_if
	# Set the transmitter in zero-if architecture in tx mode 
	# Register OSCParam
	
	def setOSCParam(self, val):
		"""Set register OSCParam"""
		self.write(REG.OSCParam, val, 8)
	def getOSCParam(self):
		"""Get register OSCParam"""
		return self.read(REG.OSCParam, 8)
	# Bits Clkout_on
	# Clkout control 
	# Bits Clkout_freq
	# Frequency of the signal provided on CLKOUT:
	#           fclkout = f_xtal                     if Clkout_freq = “00000"
	#           fclkout = f_xtal / (2 ⋅ Clkout_freq) otherwise
	#           (d): 01111 (= 427 kHz) 
	
	# Bits reserved_0
	# Register PKTParam_1
	
	def setPKTParam_1(self, val):
		"""Set register PKTParam_1"""
		self.write(REG.PKTParam_1, val, 8)
	def getPKTParam_1(self):
		"""Get register PKTParam_1"""
		return self.read(REG.PKTParam_1, 8)
	# Bits Manchester_on
	# 5.5.6.1. Enable Manchester encoding/decoding: 
	# Bits Payload_length
	# If Pkt_format=0, payload length.
	#           If Pkt_format=1, max length in Rx, not used in Tx. (d): “0000000" 
	
	# Register PKTParam_2
	
	def setPKTParam_2(self, val):
		"""Set register PKTParam_2"""
		self.write(REG.PKTParam_2, val, 8)
	def getPKTParam_2(self):
		"""Get register PKTParam_2"""
		return self.read(REG.PKTParam_2, 8)
	# Bits Node_adrs
	# Node’s local address for filtering of received packets. (d): 00h 
	# Register PKTParam_3
	
	def setPKTParam_3(self, val):
		"""Set register PKTParam_3"""
		self.write(REG.PKTParam_3, val, 8)
	def getPKTParam_3(self):
		"""Get register PKTParam_3"""
		return self.read(REG.PKTParam_3, 8)
	# Bits Pkt_format
	# Packet format: 
	# Bits Preamble_size
	# Size of the preamble to be transmitted: 
	# Bits Whitening_on
	# 5.5.6.2. Whitening/dewhitening process: 
	# Bits CRC_on
	# CRC calculation/check: 
	# Bits Adrs_filt
	# Address filtering of received packets: 
	# Bits CRC_status
	# CRC check result for current packet (READ ONLY): 
	# Register PKTParam_4
	
	def setPKTParam_4(self, val):
		"""Set register PKTParam_4"""
		self.write(REG.PKTParam_4, val, 8)
	def getPKTParam_4(self):
		"""Get register PKTParam_4"""
		return self.read(REG.PKTParam_4, 8)
	# Bits CRC_autoclr
	# FIFO auto clear if CRC failed for current packet: 
	# Bits Fifo_stby_access
	# FIFO access in standby mode: 
	# Bits reserved_0
